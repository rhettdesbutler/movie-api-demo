import { DbInstance, DbInstanceConfig } from '@cdktf/provider-aws'
import { Construct } from 'constructs'

export const createRdsDatabase = (
  scope: Construct,
  projectName: string,
  dbName: string,
  instanceClass: string,
  userName: string,
  password: string,
  port: number,
) => {
  const databaseConfiguration: DbInstanceConfig = {
    instanceClass: instanceClass,
    engine: 'mysql',
    engineVersion: '5.7',
    username: userName,
    name: dbName,
    password: password,
    port: port,
    allocatedStorage: 5,
    identifier: dbName,
    finalSnapshotIdentifier: `${dbName}-${generateRandomNumber()}`,
  }
  return new DbInstance(
    scope,
    `${projectName}-rds-instance`,
    databaseConfiguration,
  )
}

export const generateRandomNumber = (): number => {
  const max: number = 1000
  const min: number = 5

  return Number(Math.floor(Math.random() * (max - min + 1) + min))
}
