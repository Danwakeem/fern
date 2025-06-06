// Code generated by Fern. DO NOT EDIT.

package client

import (
	core "github.com/examples/fern/core"
	notificationclient "github.com/examples/fern/file/notification/client"
	service "github.com/examples/fern/file/service"
	internal "github.com/examples/fern/internal"
	option "github.com/examples/fern/option"
	http "net/http"
)

type Client struct {
	baseURL string
	caller  *internal.Caller
	header  http.Header

	Notification *notificationclient.Client
	Service      *service.Client
}

func NewClient(opts ...option.RequestOption) *Client {
	options := core.NewRequestOptions(opts...)
	return &Client{
		baseURL: options.BaseURL,
		caller: internal.NewCaller(
			&internal.CallerParams{
				Client:      options.HTTPClient,
				MaxAttempts: options.MaxAttempts,
			},
		),
		header:       options.ToHeader(),
		Notification: notificationclient.NewClient(opts...),
		Service:      service.NewClient(opts...),
	}
}
