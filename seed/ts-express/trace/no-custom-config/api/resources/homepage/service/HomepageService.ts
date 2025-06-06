/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedTrace from "../../../index";
import express from "express";
import * as serializers from "../../../../serialization/index";
import * as errors from "../../../../errors/index";

export interface HomepageServiceMethods {
    getHomepageProblems(
        req: express.Request<never, SeedTrace.ProblemId[], never, never>,
        res: {
            send: (responseBody: SeedTrace.ProblemId[]) => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction,
    ): void | Promise<void>;
    setHomepageProblems(
        req: express.Request<never, never, SeedTrace.ProblemId[], never>,
        res: {
            send: () => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction,
    ): void | Promise<void>;
}

export class HomepageService {
    private router;

    constructor(
        private readonly methods: HomepageServiceMethods,
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
        this.router.get("", async (req, res, next) => {
            try {
                await this.methods.getHomepageProblems(
                    req as any,
                    {
                        send: async (responseBody) => {
                            res.json(
                                serializers.homepage.getHomepageProblems.Response.jsonOrThrow(responseBody, {
                                    unrecognizedObjectKeys: "strip",
                                }),
                            );
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
                        `Endpoint 'getHomepageProblems' unexpectedly threw ${error.constructor.name}.` +
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
        this.router.post("", async (req, res, next) => {
            const request = serializers.homepage.setHomepageProblems.Request.parse(req.body);
            if (request.ok) {
                req.body = request.value;
                try {
                    await this.methods.setHomepageProblems(
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
                            `Endpoint 'setHomepageProblems' unexpectedly threw ${error.constructor.name}.` +
                                ` If this was intentional, please add ${error.constructor.name} to` +
                                " the endpoint's errors list in your Fern Definition.",
                        );
                        await error.send(res);
                    } else {
                        res.status(500).json("Internal Server Error");
                    }
                    next(error);
                }
            } else {
                res.status(422).json({
                    errors: request.errors.map(
                        (error) => ["request", ...error.path].join(" -> ") + ": " + error.message,
                    ),
                });
                next(request.errors);
            }
        });
        return this.router;
    }
}
