/**
 * This file was auto-generated by Fern from our API Definition.
 */

import express from "express";
import * as SeedMultiLineDocs from "../../../index";
import * as errors from "../../../../errors/index";
import * as serializers from "../../../../serialization/index";

export interface UserServiceMethods {
    getUser(
        req: express.Request<
            {
                userId: string;
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
    createUser(
        req: express.Request<never, SeedMultiLineDocs.User, SeedMultiLineDocs.CreateUserRequest, never>,
        res: {
            send: (responseBody: SeedMultiLineDocs.User) => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction,
    ): void | Promise<void>;
}

export class UserService {
    private router;

    constructor(
        private readonly methods: UserServiceMethods,
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
        this.router.get("/users/:userId", async (req, res, next) => {
            try {
                await this.methods.getUser(
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
                if (error instanceof errors.SeedMultiLineDocsError) {
                    console.warn(
                        `Endpoint 'getUser' unexpectedly threw ${error.constructor.name}.` +
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
        this.router.post("/users", async (req, res, next) => {
            const request = serializers.CreateUserRequest.parse(req.body);
            if (request.ok) {
                req.body = request.value;
                try {
                    await this.methods.createUser(
                        req as any,
                        {
                            send: async (responseBody) => {
                                res.json(
                                    serializers.User.jsonOrThrow(responseBody, { unrecognizedObjectKeys: "strip" }),
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
                    if (error instanceof errors.SeedMultiLineDocsError) {
                        console.warn(
                            `Endpoint 'createUser' unexpectedly threw ${error.constructor.name}.` +
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
