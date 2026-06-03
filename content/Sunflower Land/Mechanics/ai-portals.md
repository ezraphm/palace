---
publish: true
source: https://wiki.sfl.world/en/dev-stream/2026-04-10
tags:
  - mechanics
  - portals
  - ai
  - minigames
  - economy
type: wiki
title: AI Portals & Economy Editor
---
**Status:** Beta — available via Settings → Developer Options → Experiments

## Overview

- Players can build mini-games inside Sunflower Land using **AI prompts**
- Economy Editor allows defining resources, minting, burning, staking
- Backend (game servers, auth, security) handled by Sunflower Land API
- Players only need to build visual UI/front-end (HTML game)

## Portal AI System

- Chat-GPT-like interface to build mini-games
- Uses **Phaser** game engine
- AI generates template with score display, instructions, NPCs
- **Asset browsing**: players can select specific assets for AI to use
- **Version tracking**: revert to previous game versions
- 10+ mini-games created so far

### Games Built
- Tile Jump (multiplayer puzzle)
- Chicken Rescue V2
- Hide and Seek (Bunk and Hunter)
- Plaza Party
- Pac-Man-esque game
- Tower defense with farm animals
- Fishing game
- Sword/egg collection game

## Tokenized Game Economy

- Games can have their own currencies ("Claudecoin" in Chicken Rescue)
- Define rules for earning, spending, burning tokens
- Tokens can be traded on marketplace
- Near 1,000 sales in Chicken Rescue despite no guaranteed utility

## Restrictions

- Mini-games require team approval before going public
- No gambling or explicit content
- Join "portal builders chat" on Discord

## Getting Started

1. Go to Settings → Developer Options → Experiments → Portal AI
2. Check **Economy Template repo** for docs and examples
3. Describe your game in the text box
4. AI generates it (may take significant time)
5. Preview on testnet

---

**See also:**
- [[chicken-rescue|Chicken Rescue]]
- [[minigames|Minigames]]
