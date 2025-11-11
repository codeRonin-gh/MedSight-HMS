from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime

from src.routers import emergency, opd, wards

# --- Step 1: Create FastAPI app ---
app = FastAPI(title="MedSight HMS")

# --- Step 2: Middleware (optional) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Step 3: Include routers ---
app.include_router(emergency.router)
app.include_router(opd.router)
app.include_router(wards.router)

# --- Step 4: Root endpoint ---
@app.get("/")
def root():
    return {"message": "Welcome to MedSight HMS"}

# --- Step 5: Dashboard endpoint for Power BI or analytics ---
@app.get("/dashboard/data")
def dashboard_data():
    """
    Aggregates OPD and Wards data into one JSON structure
    for Power BI and other visualization tools.
    Converts datetime objects to ISO strings for JSON compatibility.
    """
    try:
        from src.routers import opd, wards

        def serialize(item):
            data = item.dict()
            for k, v in data.items():
                if isinstance(v, datetime):
                    data[k] = v.isoformat()
            return data

        data = {
            "appointments": [serialize(a) for a in opd.appointments_db],
            "wards": [serialize(w) for w in wards.wards_db],
        }
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
