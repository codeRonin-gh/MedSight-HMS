# MedSight HMS

Hospital Management System with Emergency, OPD, and Wards modules.
Includes dummy data for testing and Power BI integration.

## Setup

1. Clone repo:

```bash
git clone <https://github.com/codeRonin-gh/MedSight-HMS.git.>
```
# MedSight HMS
*Hospital Management System with Integrated Dashboard*  

**Tagline:** *“Transforming Hospital Management – One Patient at a Time”*

---

## Project Overview

MedSight HMS is a full-featured hospital management system designed to handle **Outpatient Departments (OPD)**, **Inpatient Wards**, and **Emergency Departments**. Built with **FastAPI** for the backend and integrated with **Power BI** for visual dashboards.  

The system focuses on:  
- Real-time patient tracking  
- Appointment scheduling  
- Ward management and bed allocation  
- Emergency patient monitoring  
- Easy integration with business intelligence tools  

> Currently uses **in-memory storage**, with plans to integrate a database for scalability.

---

## Features

- **OPD Management**
  - Register appointments  
  - Track status: Scheduled, Completed, Cancelled  
  - View upcoming appointments by doctor or date  

- **Ward Management**
  - Admit patients and allocate beds automatically  
  - Track status: Admitted, Discharged, Critical  
  - Ward-wise patient overview  

- **Emergency Department**
  - Monitor real-time patient conditions  
  - Visual occupancy tracking  
  - Prioritize urgent cases  

- **Dashboard (Power BI)**
  - KPI Cards: Total appointments, Admitted, Discharged, Critical patients  
  - Pie Charts, Bar Charts, Line Charts for visual insights  
  - Interactive slicers for filtering by ward, status, or doctor  
  - Cinematic theme with conditional formatting  

---

## Tech Stack

- **Backend:** Python, FastAPI  
- **Frontend / Dashboard:** Power BI Desktop  
- **Middleware:** CORS (via FastAPI)  
- **Dependencies:**  
  - `fastapi`  
  - `uvicorn`  
  - `pydantic`  

---

## Installation

1. **Clone the repository:**  
```bash
git clone <https://github.com/codeRonin-gh/MedSight-HMS.git.>
cd MedSight-HMS

