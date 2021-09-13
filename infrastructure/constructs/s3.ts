import { S3Bucket } from '@cdktf/provider-aws'
import { Construct } from 'constructs'

export const createBucket = (
  scope: Construct,
  bucketName: string,
  projectName: string,
) => {
  return new S3Bucket(scope, `${projectName}-s3bucket`, {
    bucket: bucketName,
  })
}
