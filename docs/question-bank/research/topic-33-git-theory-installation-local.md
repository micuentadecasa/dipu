# Topic 33 — Git: teoría, instalación/configuración y trabajo local

**Research date:** 2026-10-13 UTC  
**Primary source:** [`GIT-2.50`](../source-register.json), Git project documentation, verified entry point `https://git-scm.com/docs`  
**Environment check:** `git version 2.50.1 (Apple Git-155)`  
**Evidence boundary:** This artifact covers Git's object model, repository layout, installation/version and configuration, the working tree/index, local commits, and local references. Branch integration, rebase, merge, stash, remotes and collaboration are reserved for topics 34–35.

## Source map

The question lots cite the official Git documentation by page and section:

- [`gitglossary`](https://git-scm.com/docs/gitglossary): repository vocabulary, objects, index, working tree, refs, HEAD and detached HEAD.
- [`gitrepository-layout`](https://git-scm.com/docs/gitrepository-layout): `.git` layout, `HEAD`, `config`, `index`, `objects`, `refs` and logs.
- [`gittutorial`](https://git-scm.com/docs/gittutorial): the local workflow of working tree, index and commit history.
- [`git-config`](https://git-scm.com/docs/git-config): configuration files, scopes, keys, values, listing, setting and unsetting configuration.
- [`git-init`](https://git-scm.com/docs/git-init) and [`git-clone`](https://git-scm.com/docs/git-clone): repository creation and local clone setup.
- [`git-add`](https://git-scm.com/docs/git-add), [`git-status`](https://git-scm.com/docs/git-status), [`git-diff`](https://git-scm.com/docs/git-diff), [`git-restore`](https://git-scm.com/docs/git-restore), [`git-reset`](https://git-scm.com/docs/git-reset) and [`git-rm`](https://git-scm.com/docs/git-rm): staging, inspection, restoration and removal in the local workflow.
- [`git-commit`](https://git-scm.com/docs/git-commit), [`git-log`](https://git-scm.com/docs/git-log), [`git-show`](https://git-scm.com/docs/git-show) and [`git-reflog`](https://git-scm.com/docs/git-reflog): local commits and history/reference inspection.
- [`gitignore`](https://git-scm.com/docs/gitignore) and [`git-check-ignore`](https://git-scm.com/docs/git-check-ignore): ignore patterns and diagnosing ignored paths.

## Verified propositions

1. Git stores snapshots represented by objects. A blob stores file contents, a tree records directory entries and names, a commit identifies a snapshot and its parent history, and an annotated tag is a tag object that can carry metadata.
2. The index is the proposed next snapshot (staging area); the working tree is the checked-out files. `git add` updates the index from working-tree content, while `git commit` records the index as a new commit.
3. `git diff` compares working-tree changes with the index by default; `git diff --cached` compares the index with `HEAD`.
4. `git status` reports paths differing between `HEAD`, the index and the working tree, including untracked paths when they are not ignored.
5. `git init` creates or reinitializes a repository in a directory. `git clone` creates a new directory, initializes it and obtains a copy of an existing repository.
6. Configuration is layered. System, global, local and command-scope configuration can be queried or changed with `git config`; a more local value overrides a broader one when the same key is defined.
7. `user.name` and `user.email` identify the author/committer metadata used by commits; configuring them is not the same as authenticating to a remote.
8. `HEAD` names the currently checked-out reference or commit. `refs/heads/*` are local branch references, while the object database and references are separate repository structures.
9. `git restore` restores working-tree or index content according to its options; `git reset` has distinct modes and can move a reference as well as modify the index and working tree. These commands must not be conflated.
10. `.gitignore` patterns affect untracked path discovery; they do not remove an already tracked file. `git check-ignore` diagnoses why a path is ignored, with options for verbose/source output.
11. `git commit --amend` replaces the tip commit rather than creating an independent next commit. It is a local-history operation and should be used deliberately.
12. Reflogs record local updates to references and `HEAD` when enabled; they are local recovery/inspection records, not a replacement for shared history.

## Scope-gated objective design

The 100 researched objectives use four blocks of 25: object model/repository layout, installation and configuration, working tree/index/staging, and local commits/references. Each lot has four basic, ten intermediate and six advanced questions. No claims about remote transport, pull requests, branch integration, rebase, merge conflict resolution or stash behavior are used as Topic 33 evidence; those belong to later Git topics.
