# 📋 ImmutableU: AI-Powered Legal Contract Management Platform on Cardano Blockchain

<div align="center">

![ImmutableU Logo](https://img.shields.io/badge/ImmutableU-Legal%20Contract%20Platform-blue?style=for-the-badge)

# 🚀 Welcome to ImmutableU

**The World's First AI-Powered Legal Contract Platform Built on Cardano**
Streamline your legal workflow with blockchain security, AI assistance, and multi-signature capabilities

> _"Revolutionizing legal contracts through decentralized trust, intelligent automation, and immutable security. Powered by Cardano. Driven by AI. Designed for the future of law."_

<p align="center">
<a href="https://github.com/suzzy05/ImmutableU/blob/main/LICENSE">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT">
</a>
<img src="https://img.shields.io/badge/Cardano-Blockchain-0033AD?style=for-the-badge&logo=cardano&logoColor=white" alt="Cardano Blockchain">
</p>

</div>

<p align="center">
✨ Bridging Legal Expertise with Blockchain Trust & AI Intelligence ✨
</p>

---

[![GitHub](https://img.shields.io/badge/GitHub-suzzy05/ImmutableU-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/suzzy05/ImmutableU)
[![Cardano](https://img.shields.io/badge/Cardano-Preview%20Testnet-0066cc?style=for-the-badge&logo=cardano&logoColor=white)](https://cardano.org)
[![BlockFrost](https://img.shields.io/badge/BlockFrost-API-00d4aa?style=for-the-badge)](https://blockfrost.io)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

---

## 🚀 Overview

**ImmutableU** is a groundbreaking platform that redefines how legal contracts are created, signed, and managed. By seamlessly integrating advanced Artificial Intelligence with the immutable and transparent Cardano blockchain, ImmutableU introduces a new era of trust, efficiency, and accessibility to the legal contracting process.

From AI-assisted drafting and smart template utilization to robust multi-signature capabilities, ImmutableU empowers users through the entire contract lifecycle with unmatched transparency and control.

---

## ⚡ Quick Start

### Prerequisites

- **Node.js** v18+ and npm
- **Python** 3.10+
- **Git**
- **Cardano Wallet** (Nami, Eternl, or Flint)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/suzzy05/ImmutableU.git
   cd ImmutableU
   ```

2. **Setup Backend**
   ```bash
   cd backend
   npm install
   npx prisma generate
   npx prisma migrate dev
   npm run dev
   ```

3. **Setup Frontend**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Setup AI Service**
   ```bash
   cd mcp
   pip install -r requirements.txt
   python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Environment Variables

Create `.env` files in each directory:

**Backend (.env)**
```env
DATABASE_URL="file:./dev.db"
JWT_SECRET="your-secret-key"
PORT=3100
```

**Frontend (.env)**
```env
VITE_API_APP_BACKEND_URL=http://localhost:3100
VITE_API_BLOCKFROST_API_KEY=your-blockfrost-api-key
```

**MCP (.env)**
```env
GOOGLE_API_KEY=your-gemini-api-key
BLOCKFROST_PROJECT_ID=your-blockfrost-api-key
BLOCKFROST_BASE_URL=https://cardano-preview.blockfrost.io/api/v0
```

---

## 🏗️ System Architecture

ImmutableU is built using a modular, service-oriented architecture divided into three core systems:

### 🧠 AI Legal & Cardano Blockchain Assistant System

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Deployed%20on-Azure-0078d4?style=for-the-badge&logo=microsoft-azure&logoColor=white" alt="Deployed on Azure">
</p>

This system acts as the intelligent brain of ImmutableU. It provides:

- Legal insights for Civil, Corporate, and Property Law
- Smart contract generation and AI-driven document review
- Integration with Cardano blockchain data

➡️ [Explore the AI Legal & Cardano Assistant System : Quick Start & Setup Guide](./mcp/README.md)

---

### 💻 Frontend: ImmutableU UI

<p align="center">
<img src="https://img.shields.io/badge/React-18.3.1-61DAFB?logo=react&logoColor=white&style=for-the-badge" alt="React">
<img src="https://img.shields.io/badge/TypeScript-5.5.3-3178C6?logo=typescript&logoColor=white&style=for-the-badge" alt="TypeScript">
<img src="https://img.shields.io/badge/TailwindCSS-3.4.11-06B6D4?logo=tailwindcss&logoColor=white&style=for-the-badge" alt="TailwindCSS">
</p>

The user interface is clean, responsive, and intuitive. Features include:

- Wallet connection and digital signature management
- Dynamic contract templates
- AI-assistance embedded in the UI


---

### ⚙️ Backend: Smart Contract Management API

<p align="center">
<img src="https://img.shields.io/badge/Node.js-v18+-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js">
<img src="https://img.shields.io/badge/TypeScript-API-3178C6?logo=typescript&logoColor=white&style=for-the-badge" alt="TypeScript">
<img src="https://img.shields.io/badge/PostgreSQL-DB-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
</p>

This backend system:

- Manages user authentication & role-based access
- Handles blockchain document verification & digital signatures
- Ensures full contract lifecycle security



---

## ✨ Key Features

### 🤖 AI-Powered Legal Assistant
- **Google Gemini Integration** - Advanced AI for legal document analysis
- **Multi-Domain Expertise** - Civil Law, Corporate Law, Property Law
- **Smart Contract Generation** - AI-assisted contract creation
- **Legal Query Resolution** - Instant answers to legal questions

### 🔐 Blockchain Security
- **Cardano Integration** - Immutable contract storage
- **BlockFrost API** - Seamless blockchain interaction
- **Multi-Signature Support** - Secure contract signing
- **Transaction Verification** - Transparent audit trail

### 💼 Contract Management
- **Template Library** - Pre-built legal templates
- **Digital Signatures** - Wallet-based authentication
- **Real-time Collaboration** - Multi-party contract editing
- **Status Tracking** - Complete contract lifecycle management

### 🎨 Modern UI/UX
- **React + TypeScript** - Type-safe frontend development
- **TailwindCSS** - Beautiful, responsive design
- **shadcn/ui Components** - Modern UI component library
- **MeshSDK Integration** - Seamless wallet connectivity

---

## 🚀 Deployment

### Recommended Stack

**Frontend:** Vercel (Free)
- Automatic deployments from GitHub
- Global CDN
- Custom domains

**Backend:** Render (Free Tier)
- Node.js hosting
- Automatic SSL
- Environment variables

**AI Service:** Render (Free Tier)
- Python hosting
- FastAPI support
- Auto-scaling

### Deployment Steps

1. **Push to GitHub** ✅ (Already done!)
2. **Deploy Frontend on Vercel**
   - Connect GitHub repository
   - Set root directory to `frontend`
   - Add environment variables
   - Deploy!

3. **Deploy Backend on Render**
   - Create new Web Service
   - Set root directory to `backend`
   - Add build command: `npm install && npx prisma generate`
   - Add environment variables
   - Deploy!

4. **Deploy AI Service on Render**
   - Create new Web Service
   - Set root directory to `mcp`
   - Add build command: `pip install -r requirements.txt`
   - Add environment variables
   - Deploy!

---

## 🙏 Acknowledgments

We extend our deepest gratitude to the following technologies, communities, and resources that were instrumental in bringing **ImmutableU** to life:

- **Cardano Foundation** — For providing the foundational blockchain infrastructure.
- **BlockFrost** — For enabling seamless API access to the Cardano blockchain.
- **Mesh SDK** — For Cardano integration tools.
- **Aiken** — For smart contract development tools.
- **The Incredible Open-Source Community** — For invaluable tools and libraries.

---
</p>
