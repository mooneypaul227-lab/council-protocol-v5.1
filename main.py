"""
Council Protocol v5.1 - Security Management
Main application entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Council Protocol v5.1",
    description="Security Management API",
    version="5.1.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "council-protocol-v5.1",
            "version": "5.1.0"
        }
    )

# API status endpoint
@app.get("/api/status")
async def api_status():
    """API status endpoint"""
    return {
        "status": "operational",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "version": "5.1.0"
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Council Protocol v5.1 - Security Management API",
        "endpoints": {
            "health": "/health",
            "status": "/api/status",
            "docs": "/docs",
            "api_docs": "/api/docs"
        }
    }

# API documentation
@app.get("/api/docs")
async def api_documentation():
    """API documentation endpoint"""
    return {
        "api_version": "5.1.0",
        "title": "Council Protocol v5.1",
        "description": "Security Management API",
        "endpoints": [
            {"path": "/health", "method": "GET", "description": "Health check"},
            {"path": "/api/status", "method": "GET", "description": "API status"},
            {"path": "/docs", "method": "GET", "description": "Interactive documentation (Swagger UI)"},
            {"path": "/redoc", "method": "GET", "description": "API documentation (ReDoc)"}
        ]
    }

# Example endpoint for security management
@app.get("/api/security/status")
async def security_status():
    """Get current security status"""
    return {
        "timestamp": "2026-07-13T23:35:00Z",
        "security_level": "operational",
        "protocols_active": [
            "authentication",
            "authorization",
            "encryption",
            "audit_logging"
        ],
        "last_security_audit": "2026-07-13"
    }

if __name__ == "__main__":
    logger.info("Starting Council Protocol v5.1")
    import uvicorn
    uvicorn.run(
        app,
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", 8000)),
        reload=os.getenv("ENVIRONMENT", "development") == "development"
    )
