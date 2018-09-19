/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

import * as SchemaValidator from 'z-schema';
import { parseJsonPointer } from '../ref/jsonpath';
import { ReadUri, ResolveUri } from '../ref/uri';
import { QuickDataSource } from '../data-store/data-store';
import { Parse } from '../ref/yaml';
import { CreatePerFilePlugin, PipelinePlugin } from "./common";
import { Channel } from "../message";
import { OperationAbortedException } from '../exception';

export function GetPlugin_SchemaValidatorSwagger(): PipelinePlugin {
  const validator = new SchemaValidator({ breakOnFirstError: false });

  const extendedSwaggerSchema = require('./swagger-extensions.json');
  (validator as any).setRemoteReference("http://json.schemastore.org/swagger-2.0", require("./swagger.json"));
  (validator as any).setRemoteReference("https://raw.githubusercontent.com/Azure/autorest/master/schema/example-schema.json", require("./example-schema.json"));
  return CreatePerFilePlugin(async config => async (fileIn, sink) => {
    const obj = fileIn.ReadObject<any>();
    const errors = await new Promise<{ code: string, params: string[], message: string, path: string }[] | null>(res => validator.validate(obj, extendedSwaggerSchema, (err, valid) => res(valid ? null : err)));
    if (errors !== null) {
      for (const error of errors) {
        config.Message({
          Channel: Channel.Error,
          Details: error,
          Plugin: 'schema-validator-swagger',
          Source: [{ document: fileIn.key, Position: { path: parseJsonPointer(error.path) } as any }],
          Text: `Schema violation: ${error.message}`
        });
      }
      throw new OperationAbortedException();
    }
    return await sink.Forward(fileIn.Description, fileIn);
  });
}

export function GetPlugin_SchemaValidatorOpenApi(): PipelinePlugin {
  const validator = new SchemaValidator({ breakOnFirstError: false });

  const extendedOpenApiSchema = require('./openapi3-schema.json');
  return CreatePerFilePlugin(async config => async (fileIn, sink) => {
    const obj = fileIn.ReadObject<any>();
    const errors = await new Promise<{ code: string, params: string[], message: string, path: string }[] | null>(res => validator.validate(obj, extendedOpenApiSchema, (err, valid) => res(valid ? null : err)));
    if (errors !== null) {
      for (const error of errors) {
        config.Message({
          Channel: Channel.Error,
          Details: error,
          Plugin: 'schema-validator-openapi',
          Source: [{ document: fileIn.key, Position: { path: parseJsonPointer(error.path) } as any }],
          Text: `Schema violation: ${error.message}`
        });
      }
      throw new OperationAbortedException();
    }
    return await sink.Forward(fileIn.Description, fileIn);
  });
}