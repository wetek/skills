---
name: web-ui
description: Web UI interaction, scroll, focus, URL state, and panel guidelines. Load when building, modifying, or reviewing frontend components, pages, forms, tables, or modals.
---

# Web UI guidelines

Apply these rules when building or reviewing web interfaces.

## 1. Synchronous submit locking

- Lock form submissions and async action buttons synchronously on the first interaction (such as with a synchronous ref guard before async state updates flush) so rapid double-clicks cannot fire duplicate requests.
- Render a spinner alongside a clear progress label while the action is in flight.
- Keep the control disabled and non-interactive (`disabled`, `pointer-events-none`, `cursor-not-allowed`) until the destination view mounts or the operation settles.

## 2. Explicit confirmation for destructive or high-impact actions

- Any action that deletes data, removes a user, disconnects an integration, discards unsaved work, or interrupts a running job or session must require explicit user confirmation via a confirmation modal before executing.

## 3. Scroll hierarchy and sticky panels

- Keep primary content and result lists at natural document height without nested vertical scroll containers.
- On sticky detail panels or sidebars that require internal scrolling, set `overscroll-behavior-y: auto` so scrolling chains naturally back to the main window at the top and bottom boundaries.

## 4. Conflict-free focus styles and semantic tokens

- Style components using semantic theme tokens (colors, typography, spacing, shadows) rather than hardcoded hex values or arbitrary pixel utilities.
- Wrap global focus-visible defaults in `:where(:focus-visible)` (`0` specificity) so composite inputs and custom controls never render double focus outlines.

## 5. URL-driven view state and adjustable panels

- Store list filters, search queries, pagination, and table sort order (`?sort=...&order=asc|desc`) in URL query parameters so views are bookmarkable and shareable, and expose sortable column headers on data tables where appropriate.
- Where split panes, side sheets, or resizable modal panels are used, make them adjustable (pointer drag, keyboard arrows, double-click to reset) and persist layout sizes locally for the user.

## 6. Multi-viewport and console verification

- Verify modified routes across desktop and mobile viewports (including open modals, sheets, and drawers) and inspect both the server terminal and browser console for HTTP `4xx`/`5xx` or runtime errors.
