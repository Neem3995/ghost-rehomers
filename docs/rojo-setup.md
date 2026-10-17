# Verified Rojo setup — 2026-10-17

System checked: Windows 11 Home x64, build 26200; Roblox Studio 0.743.0.7431133.

Recommended baseline: matching **Rojo 7.7.1 CLI and Studio plugin**, the current official stable release checked for this repair. The [release notes](https://github.com/rojo-rbx/rojo/releases/tag/v7.7.1) include Windows path/file-watcher fixes; no evidence justified a downgrade. This is a verified working baseline, not a guarantee against future bugs.

## Installed and preserved

- Existing Rokit CLI binary matched the extracted official Windows x86_64 release byte-for-byte; retained it.
- Reinstalled the official release Rojo.rbxm as `%LOCALAPPDATA%\Roblox\Plugins\RojoManagedPlugin.rbxm`, then restarted Studio.
- Official Windows ZIP SHA256: `d4dfa3493a1613a43fc87312d6dac660d7c8bf38e6a99aa5dcd0d26154ba0b82`.
- Installed official plugin SHA256: `50a8d83db87deab4d65fd6100eb74396de232355b1ae89c641035d02c49db6f4`. Both download digests matched GitHub release metadata.
- Prior plugin and place backed up under `%LOCALAPPDATA%\Codex\RojoRepair\20261017-115709`. Place saved before restart and again after verification. Uncommitted source and branch preserved; no src/ edits.
- Disabled experimental Auto Connect Playtest Server and Open Scripts Externally. On disconnecting to inspect the unlocked control, Two-Way Sync was enabled; explicitly disabled it too. This can otherwise write Studio edits back into the files Claude edits. Use one-way Edit-mode sync followed by a fresh playtest.

## Launch once; reuse the server

The project's rokit.toml already pins 7.7.1. The repair started the actual installed executable directly with an absolute project path and loopback binding, avoiding shell PATH and current-directory ambiguity:

```powershell
& "$env:USERPROFILE\.rokit\tool-storage\rojo-rbx\rojo\7.7.1\rojo.exe" serve "C:\Users\hoese\Desktop\Roblox\ghost-rehomers\default.project.json" --address 127.0.0.1 --port 34872
```

A hidden standalone server was left running for this session. Logs are in the backup directory as rojo-server.stdout.log and rojo-server.stderr.log. Do not start another server if this port already serves the intended project. Check the command, project and listener before restarting. A Rokit shim plus its child process is not itself evidence of duplicate servers.

In Studio: Rojo panel -> localhost:34872 -> Connect. Confirm project name ghost-rehomers. Confirmation Behavior is currently Never, so an Accept dialog need not appear. Rojo is separate from Studio MCP and Git: an MCP connection or Git commit does not prove Rojo sync.

## Verification actually performed

- One direct Rojo process listening on 127.0.0.1:34872; server stderr empty at check.
- Studio panel showed connected ghost-rehomers on localhost:34872 after plugin reload.
- Reversible data-only probe: appended a unique marker to unused ghost personality text; Studio Data.Ghosts Source received it. Restored original JSON bytes; Studio Source removed the marker. No probe content retained.
- All 10 loaded scripts matched normalized local source length and Adler-32 before restart/save and after reconnect. This is a source-consistency check, not cryptographic proof of runtime behavior.
- Synced place saved to disk; gameplay/device/co-op acceptance was not run during this repair.

If sync goes stale again: stop play, check project/port and logs, compare one loaded script with its local file, then reconnect. Do not edit Rojo-managed scripts directly through MCP or Studio; disk files remain authoritative. The earlier stale-sync cause was not conclusively reproduced, so this repair does not claim a confirmed root cause.

Official installation reference: [Rojo installation](https://rojo.space/docs/v7/getting-started/installation/).
