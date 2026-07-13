"""Tests for main application"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestHealthCheck:
    """Health check endpoint tests"""
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
        assert response.json()["service"] == "council-protocol-v5.1"

class TestAPIStatus:
    """API status endpoint tests"""
    
    def test_api_status(self):
        """Test API status endpoint"""
        response = client.get("/api/status")
        assert response.status_code == 200
        assert response.json()["status"] == "operational"
        assert "version" in response.json()

class TestRootEndpoint:
    """Root endpoint tests"""
    
    def test_root(self):
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()
        assert "endpoints" in response.json()

class TestSecurityStatus:
    """Security status endpoint tests"""
    
    def test_security_status(self):
        """Test security status endpoint"""
        response = client.get("/api/security/status")
        assert response.status_code == 200
        assert "security_level" in response.json()
        assert "protocols_active" in response.json()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
