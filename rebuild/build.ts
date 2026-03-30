// @ts-ignore
import fs from 'fs';

const REFERENCES_PATH = 'rebuild/references';
const SRC_PATH = 'rebuild/src';


const { createLogger, format, transports } = require('winston');

const logger = createLogger({
    level: 'info',
    format: format.combine(
        //format.timestamp({
        //    format: 'YYYY-MM-DD HH:mm:ss'
        //}),
        format.errors({ stack: true }),
        format.splat(),
        format.json()
    ),
    //defaultMeta: { service: 'your-service-name' },
    transports: [
        //
        // - Write to all logs with level `info` and below to `quick-start-combined.log`.
        // - Write all logs error (and below) to `quick-start-error.log`.
        //
        //new transports.File({ filename: 'quick-start-error.log', level: 'error' }),
        //new transports.File({ filename: 'quick-start-combined.log' })
    ]
});

//
// If we're not in production then **ALSO** log to the `console`
// with the colorized simple format.
//
if (process.env.NODE_ENV !== 'production') {
    logger.add(new transports.Console({
        format: format.combine(
            format.colorize(),
            format.simple()
        )
    }));
}

//const exampleFileContent = fs.readFileSync('.gitignore','utf8');
//console.log(exampleFileContent);

const buildDirContent = fs.readdirSync(SRC_PATH);
var header;
var footer;


try{
    header = fs.readFileSync(SRC_PATH + '/header.html','utf8');
} catch (error) {
    logger.warn("No header file found. Continuing without.")
    logger.debug(error);
    header = "";
}
try{
    footer = fs.readFileSync('rebuild/src/footer.html','utf8');
} catch (error) {
    logger.warn("No footer file found. Continuing without.")
    logger.debug(error);
    footer = "";
}

logger.info("*** BUILD DIR ***********")
logger.info(buildDirContent);
logger.info("*** HEADER CONTENT ******")
logger.info(header);
logger.info("*** FOOTER CONTENT ******")
logger.info(footer);
logger.info("*** END *****************")
