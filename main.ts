import { App } from 'cdktf'
import { RBTestMoviesApiStack } from './infrastructure/stacks/rhett-test-movies-api-stack.stack'
import { RhettTestMoviesApiStackName } from './infrastructure/utils/stack-names'

const path = require('path')

const currentWorkingDir: string = path.join(__dirname, '/dist')

const app = new App({ outdir: currentWorkingDir })

new RBTestMoviesApiStack(app, RhettTestMoviesApiStackName)
app.synth()
