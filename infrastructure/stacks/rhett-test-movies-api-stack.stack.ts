import { Construct } from 'constructs'
import { TerraformStack } from 'cdktf'
import {
  AwsProvider,
  LambdaFunctionEnvironment,
  LambdaFunction,
} from '@cdktf/provider-aws'
import { createBucket } from '../constructs/s3'
import { createRdsDatabase } from '../constructs/rds'
import { createLambdaFunction } from '../constructs/lambda'
import { rhettTestMoviesApiProjectName } from '../utils/project-name'
import { createApiGateway } from '../constructs/api-gateway'

export class RBTestMoviesApiStack extends TerraformStack {
  constructor(scope: Construct, name: string) {
    super(scope, name)

    const projectName: string = rhettTestMoviesApiProjectName
    const bucketName: string =
      `${rhettTestMoviesApiProjectName}-bucket`.toLowerCase()
    const region: string = 'eu-west-1'

    // AWS
    const provider = new AwsProvider(
      this,
      `${rhettTestMoviesApiProjectName}-AwsProvider`,
      {
        region: region,
      },
    )

    // RDS Connections
    const dbName: string = 'rhetttestdb'
    const userName: string = 'rhettroottest'
    const instanceClass: string = 'db.t3.micro'
    const password: string = 'rbu!GaTest&94Egg'
    const port: number = 4387

    createBucket(this, bucketName, projectName)

    createRdsDatabase(
      this,
      projectName,
      dbName,
      instanceClass,
      userName,
      password,
      port,
    )

    const lambdaEnvVariables: LambdaFunctionEnvironment[] = [
      {
        variables: {
          REGION: region,
          DATA_BUCKET: bucketName,
          PROJECT_NAME: projectName,
          DB_USERNAME: userName,
          DB_NAME: dbName,
          DB_PASSWORD: password,
          DB_PORT: String(port),
        },
      },
    ]

    // Lambda Function for User API Calls:
    const movieApiCodePath: string = 'projects/movies_api/handlers'
    const codeFilename: string = 'movie_api.zip'

    const apiLambdaFunction: LambdaFunction = createLambdaFunction(
      this,
      projectName,
      provider,
      bucketName,
      movieApiCodePath,
      codeFilename,
      lambdaEnvVariables,
    )

    // API GateWay
    createApiGateway(this, projectName, apiLambdaFunction)
  }
}
