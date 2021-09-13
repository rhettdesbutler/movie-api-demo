import { IamRole, AwsProvider, IamRoleConfig } from '@cdktf/provider-aws'
import { Construct } from 'constructs'

export const createBaseRole = (
  scope: Construct,
  projectName: string,
  provider: AwsProvider,
) => {
  const iamRoleConfig: IamRoleConfig = {
    name: `${projectName}-iam-role`,
    provider: provider,
    assumeRolePolicy: JSON.stringify({
      Version: '2012-10-17',
      Statement: [
        {
          Action: 'sts:AssumeRole',
          Principal: {
            Service: 'lambda.amazonaws.com',
          },
          Effect: 'Allow',
        },
      ],
    }),
  }
  return new IamRole(scope, `${projectName}-IamRole`, iamRoleConfig)
}
