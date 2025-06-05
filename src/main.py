"""
Application Entry Point

This file serves as the main entry point for the Alyf API Server.
It initializes the FastAPI application, registers all routes from the controllers,
sets up middleware, error handlers, and starts the server.

Key responsibilities:
- Configure and initialize the FastAPI app
- Register all routes from the APC, Member, and Internal controllers
- Set up authentication middleware
- Configure CORS
- Set up error handling
- Initialize database connections
- Start the application server
""" 