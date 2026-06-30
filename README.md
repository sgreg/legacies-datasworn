# Ironsworn: Legacies hackish Datasworn ruleset

**State**: *Playtest Alpha 1B, 2026-06-22*

> [!NOTE] 
> This is intended for Iron Vault (meaning that's what I've tested it with), and by no means is it claimed to be great and anything else than a quick, hackish way to have _some_ support for the Legacies playtest available.
> Not all concepts Legacies introduces are easily supported by Iron Vault, so some compromises are necessary. 

## Content

- Approaches as moves:
  - Take Action, Gain Advantage, Suffer Misfortune
  - Undertake a Quest, Reach a Milestone, Resolve a Quest, Forsake a Quest
  - Take on a Challenge, Resolve a Challenge
  - Spend Boons
  - Pass Time
  - Test Your Legacy, End Your Legacy
- Condition meters added to the character sheet
  - Boons (0-99)
  - Legacy Segments (-12 to +12 to account for locked segments)
  - Legacy Tier (0-5)
  - Position (+1 for favored, 0 for pressured, -1 for desperate)
  - Momentum as before
  - OG Ironsworn Health, Spirit, and Supply (plus the legacy tracks) cause that's just how it is. Ignore them.
- Assets
  - **Impacts are added as assets**, so Health, Spirit, and Supply all have their own asset card that needs to be added to the character. Note that they're reversed, so you take on a meter to add an impact and suffer on a meter to clear it. Not great, but that's how it is.
  - Resources are also added as assets. There are 4 individual resources, as you cannot add the same asset twice in Iron Vault. If four won't be enough, go break some of them ;)
- Oracles
  - Action Codex
    - Fight
    - Interact
    - Journey
  - Encounter Codex
    - Elder Beast (thanks [@hekau-chasut](https://github.com/hekau-chasut))
    - Undying
  - preliminary Action+Theme

No mechanics for advantages / misfortunes, my suggestion is to use out-of-character comments for that.

## Set up in Iron Vault
Make sure you have the Homebrew feature enabled in Iron Vault.

> [!NOTE]
> Do NOT create a new note in Obsidian and copy the content from the `legacies-datasworn-XX.YYYYYY.ZZ.json` in there!
> Either select the right folder when you download the file, or copy the file itself in there after you downloaded it.

### Campaign specific
The easiest way is to create a new classic Ironsworn campagin as always, and once that's set up, create the `Custom Content` folder inside the campaign's folder, and download the `legacies-datasworn-XX.YYYYYY.ZZ.json` file from here in there.

### Global Homebrew
Another option is to download the file to the vault's `Homebrew/` folder and set up a new campaign with a custom ruleset.

To add the Legacies stuff, select "Custom" in the campaign setup, click the "Configure" button next to it, and add in the textbox within the popup:
```
*:classic/**
*:legacies/**
```

In case you also want to add things from Delve and Lodestar, make that:
```
*:classic/**
*:delve/**
*:lodestar/**
*:legacies/**
```

To confirm it works, search for "Take Action" in that same popup. It should show a checkmark next to the Take Action result.

