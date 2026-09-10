# Getting Started

Step by step, in order. Steps 1-2 are one-time machine setup. Step 3 onward
is where the workspace configures itself for you.

## 1. Prerequisites (do this first, outside this folder)

- **Claude Code** installed and signed in. If you don't have it yet, ask
  whoever gave you this folder for the install link.
- **Git** installed (`git --version` in a terminal should print a version).
- **GitHub access to `g2webservices/greenlight`.** Request this now if you
  haven't already — it can take time to get approved, and you can continue
  with everything else while you wait.

## 2. Run the bootstrap script

Open a terminal, go into this folder, and run:

```
./bootstrap.sh
```

This checks that git and Claude Code are available, tells you plainly if
something's missing, and tries to clone the Greenlight repo if your access is
already active (it's fine if it isn't yet — the script says so and moves on,
nothing fails).

## 3. Open the workspace in Claude Code

From the same folder:

```
claude
```

(Or open this folder in the Claude Code VS Code / desktop extension.)

## 4. Run `/setup`

Type `/setup` and press enter. From here it's a conversation, not a checklist
you have to remember — Claude will:

- Explain what the workspace is for
- Try cloning the Greenlight repo again if step 2 couldn't (and tell you
  exactly what to do if access still isn't granted)
- Offer to clone the Unified Platform design-system repo, for building
  re-platformed screens to the same visual standard
- Tell you how to connect Figma (this one requires you to click through your
  own login — Claude can't do it for you)
- Check the workspace is set up correctly and tell you if anything's wrong
- Walk you through what each skill does and suggest where to start

Just answer what it asks. If you don't know an answer, say so — it will
either make a reasonable default choice or tell you what it needs from you
specifically.

## 5. Do your first piece of real work

Once `/setup` finishes, start with whatever Greenlight requirement is in
front of you. The lowest-friction starting point is:

```
/mini-prd
```

for a short requirement doc. For something bigger, use `/discovery` first,
then `/prd`, then `/spec` — Claude will explain the difference if you ask.

## If something goes wrong

- **`/setup` says a step failed** — read what it says; it's usually "you
  don't have access yet" or "this needs your own login," not something
  Claude can fix by retrying.
- **You want to redo setup** — just run `/setup` again. It picks up where
  things are still incomplete rather than repeating what already worked.
- **Something in this guide doesn't match what you see** — ask Claude
  directly in the chat ("this doesn't match the guide, what's going on") —
  it can read its own configuration and tell you what's actually true.
