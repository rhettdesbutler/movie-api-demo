import { Apigatewayv2Api, LambdaFunction } from '@cdktf/provider-aws'
import { Construct } from 'constructs'

export const createApiGateway = (
  scope: Construct,
  projectName: string,
  lambdaFunction: LambdaFunction,
) => {
  return new Apigatewayv2Api(scope, `${projectName}-ApiGateWay`, {
    name: `${projectName}-apiGateWay`,
    protocolType: 'HTTP',
    target: lambdaFunction.arn,
  })
}
