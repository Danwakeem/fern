/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedTrace from "../../../index";
import express from "express";
import * as errors from "../../../../errors/index";

export interface SubmissionServiceMethods {
    createExecutionSession(
        req: express.Request<
            {
                language: SeedTrace.Language;
            },
            SeedTrace.ExecutionSessionResponse,
            never,
            never
        >,
        res: {
            send: (responseBody: SeedTrace.ExecutionSessionResponse) => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction,
    ): void | Promise<void>;
    getExecutionSession(
        req: express.Request<
            {
                sessionId: string;
            },
            SeedTrace.ExecutionSessionResponse | undefined,
            never,
            never
        >,
        res: {
            send: (responseBody: SeedTrace.ExecutionSessionResponse | undefined) => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction,
    ): void | Promise<void>;
    stopExecutionSession(
        req: express.Request<
            {
                sessionId: string;
            },
            never,
            never,
            never
        >,
        res: {
            send: () => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction,
    ): void | Promise<void>;
    getExecutionSessionsState(
        req: express.Request<never, SeedTrace.GetExecutionSessionStateResponse, never, never>,
        res: {
            send: (responseBody: SeedTrace.GetExecutionSessionStateResponse) => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction,
    ): void | Promise<void>;
}

/**
 * Responsible for spinning up and spinning down execution.
 */
export class SubmissionService {
    private router;

    constructor(
        private readonly methods: SubmissionServiceMethods,
        middleware: express.RequestHandler[] = [],
    ) {
        this.router = express.Router({ mergeParams: true }).use(
            express.json({
                strict: false,
            }),
            ...middleware,
        );
    }

    public addMiddleware(handler: express.RequestHandler): this {
        this.router.use(handler);
        return this;
    }

    public toRouter(): express.Router {
        this.router.post("/create-session/:language", async (req, res, next) => {
            try {
                await this.methods.createExecutionSession(
                    req as any,
                    {
                        send: async (responseBody) => {
                            res.json(responseBody);
                        },
                        cookie: res.cookie.bind(res),
                        locals: res.locals,
                    },
                    next,
                );
                if (res.writableEnded) {
                    next();
                }
            } catch (error) {
                if (error instanceof errors.SeedTraceError) {
                    console.warn(
                        `Endpoint 'createExecutionSession' unexpectedly threw ${error.constructor.name}.` +
                            ` If this was intentional, please add ${error.constructor.name} to` +
                            " the endpoint's errors list in your Fern Definition.",
                    );
                    await error.send(res);
                } else {
                    res.status(500).json("Internal Server Error");
                }
                next(error);
            }
        });
        this.router.get("/:sessionId", async (req, res, next) => {
            try {
                await this.methods.getExecutionSession(
                    req as any,
                    {
                        send: async (responseBody) => {
                            res.json(responseBody);
                        },
                        cookie: res.cookie.bind(res),
                        locals: res.locals,
                    },
                    next,
                );
                if (res.writableEnded) {
                    next();
                }
            } catch (error) {
                if (error instanceof errors.SeedTraceError) {
                    console.warn(
                        `Endpoint 'getExecutionSession' unexpectedly threw ${error.constructor.name}.` +
                            ` If this was intentional, please add ${error.constructor.name} to` +
                            " the endpoint's errors list in your Fern Definition.",
                    );
                    await error.send(res);
                } else {
                    res.status(500).json("Internal Server Error");
                }
                next(error);
            }
        });
        this.router.delete("/stop/:sessionId", async (req, res, next) => {
            try {
                await this.methods.stopExecutionSession(
                    req as any,
                    {
                        send: async () => {
                            res.sendStatus(204);
                        },
                        cookie: res.cookie.bind(res),
                        locals: res.locals,
                    },
                    next,
                );
                if (res.writableEnded) {
                    next();
                }
            } catch (error) {
                if (error instanceof errors.SeedTraceError) {
                    console.warn(
                        `Endpoint 'stopExecutionSession' unexpectedly threw ${error.constructor.name}.` +
                            ` If this was intentional, please add ${error.constructor.name} to` +
                            " the endpoint's errors list in your Fern Definition.",
                    );
                    await error.send(res);
                } else {
                    res.status(500).json("Internal Server Error");
                }
                next(error);
            }
        });
        this.router.get("/execution-sessions-state", async (req, res, next) => {
            try {
                await this.methods.getExecutionSessionsState(
                    req as any,
                    {
                        send: async (responseBody) => {
                            res.json(responseBody);
                        },
                        cookie: res.cookie.bind(res),
                        locals: res.locals,
                    },
                    next,
                );
                if (res.writableEnded) {
                    next();
                }
            } catch (error) {
                if (error instanceof errors.SeedTraceError) {
                    console.warn(
                        `Endpoint 'getExecutionSessionsState' unexpectedly threw ${error.constructor.name}.` +
                            ` If this was intentional, please add ${error.constructor.name} to` +
                            " the endpoint's errors list in your Fern Definition.",
                    );
                    await error.send(res);
                } else {
                    res.status(500).json("Internal Server Error");
                }
                next(error);
            }
        });
        return this.router;
    }
}
