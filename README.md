# RentChain – Rental Agreement Management

A beginner-friendly Flask + SQLite academic project.

## Features
- Landlord and tenant registration/login
- Create rental agreements
- Tenant can accept/reject/pending an agreement
- Agreement details and rent-record history
- SHA-256 document fingerprint verification
- Hash-linked demo ledger for agreement and payment events
- Dashboard and ledger history

## Important project limitation
The ledger in this starter project is stored in SQLite and demonstrates hash-linked records. It is **not a decentralized blockchain** and is not tamper-proof against someone who can alter the database. For a real blockchain extension, deploy a Solidity smart contract to a test network and store agreement hashes on-chain. This project does not provide legally compliant e-signatures or process actual rent payments.

## Requirements
- Python 3.10 or newer
- VS Code recommended

## Run on Windows
1. Extract the ZIP file.
2. Open the `RentChain` folder in VS Code.
3. Open Terminal → New Terminal.
4. Create a virtual environment:
   ```powershell
   py -m venv .venv
   ```
5. Activate it:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, use Command Prompt and run:
   ```bat
   .venv\Scripts\activate.bat
   ```
6. Install packages:
   ```powershell
   python -m pip install -r requirements.txt
   ```
7. Start the app:
   ```powershell
   python app.py
   ```
8. Open `http://127.0.0.1:5000` in your browser.

## First test
1. Register a landlord account using one email.
2. Register a tenant account using a different email.
3. Log in as landlord and create an agreement using the tenant's registered email.
4. Open the agreement details and note the agreement ID.
5. Log out and log in as tenant to accept or reject the agreement.
6. Add a rent record and test the Verify page.

## Reset demo data
Stop the app and delete `rentchain.db`. The database will be recreated on the next start.

## Security before real use
Change `RENTCHAIN_SECRET`, use HTTPS, add CSRF protection and rate limiting, review access controls, and obtain legal review. Do not use real personal or financial information in a classroom demo.
