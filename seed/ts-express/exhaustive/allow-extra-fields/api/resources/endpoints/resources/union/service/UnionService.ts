/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedExhaustive from "../../../../../index";
import express from "express";
import * as serializers from "../../../../../../serialization/index";
import * as errors from "../../../../../../errors/index";

export interface UnionServiceMethods {
    getAndReturnUnion(
        req: express.Request<never, SeedExhaustive.types.Animal, SeedExhaustive.types.Animal, never>,
        res: {
            send: (responseBody: SeedExhaustive.types.Animal) => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction,
    ): void | Promise<void>;
}

export class UnionService {
    private router;

    constructor(
        private readonly methods: UnionServiceMethods,
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
        this.router.post("", async (req, res, next) => {
            const request = serializers.types.Animal.parse(req.body);
            if (request.ok) {
                req.body = request.value;
                try {
                    await this.methods.getAndReturnUnion(
                        req as any,
                        {
                            send: async (responseBody) => {
                                res.json(
                                    serializers.types.Animal.jsonOrThrow(responseBody, {
                                        unrecognizedObjectKeys: "passthrough",
                                        allowUnrecognizedUnionMembers: true,
                                        allowUnrecognizedEnumValues: true,
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
                    if (error instanceof errors.SeedExhaustiveError) {
                        console.warn(
                            `Endpoint 'getAndReturnUnion' unexpectedly threw ${error.constructor.name}.` +
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
