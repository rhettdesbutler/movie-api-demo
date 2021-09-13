import {
  LambdaFunction,
  AwsProvider,
  LambdaFunctionConfig,
  LambdaFunctionEnvironment,
} from '@cdktf/provider-aws'
import { Construct } from 'constructs'
import { createBaseRole } from './iam-roles'
import { LambdaRuntimes } from '../../common/runtimes'
// import { TerraformAsset, AssetType } from 'cdktf'
// import { S3BucketObject } from '../../.gen/providers/aws/s3-bucket-object'
//import * as path from 'path'

export const createLambdaFunction = (
  scope: Construct,
  projectName: string,
  awsProvider: AwsProvider,
  codeBucket: string,
  codePath: string,
  codeFileName: string,
  environmentalVariables?: LambdaFunctionEnvironment[],
) => {
  const baseRole: any = createBaseRole(scope, projectName, awsProvider)

  //const actualCodePath: string = path.resolve(__dirname, '../../../', codePath)

  // const asset = new TerraformAsset(scope, `${projectName}-codeAsset`, {
  //   path: actualCodePath,
  //   type: AssetType.DIRECTORY,
  // })

  // console.log(asset.path)
  // console.log(asset.fileName)

  // const lambdaArchive = new S3BucketObject(
  //   scope,
  //   `${projectName}-LambdaArchive`,
  //   {
  //     bucket: codeBucket,
  //     key: `${codeFileName}`,
  //     source: actualCodePath,
  //   },
  // )

  const lambdaConfiguration: LambdaFunctionConfig = {
    functionName: `${projectName}-api-function`,
    role: baseRole.arn.toString(),
    memorySize: 128,
    timeout: 15,
    environment: environmentalVariables,
    s3Bucket: codeBucket,
    s3Key: codeFileName,
    runtime: LambdaRuntimes.Python(),
    handler: `${codePath}/index.py`,
  }

  return new LambdaFunction(
    scope,
    `${projectName}-lambda-function`,
    lambdaConfiguration,
  )
}
