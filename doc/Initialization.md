# Initializing MPD (once per system)

> [!WARNING]
> If you have not already [installed MPD](Installation.md), you must do that first.

You must initialize MPD on the system where you intend to use it.
This needs to be done only once per system and is achieved by typing:

```console
$ spack mpd init
```

A successful initialization will print something like:

``` console
==> Using Spack instance at /scratch/knoepfel/spack
==> Added repo with namespace 'local-mpd'.
```

At this point, you may safely use any MPD subcommand.

### Reinitialization

Reinitialization of MPD on a given system is not yet natively
supported.  If you execute `spack mpd init` again on a system that you
have already initialized, you will see something like:

``` console
==> Using Spack instance at /scratch/knoepfel/spack
==> Warning: MPD already initialized on this system (/home/knoepfel/.mpd)
```

If you wish to "start from scratch" you may force a reinitialization, which will remove
all existing projects:

```console
$ spack mpd init -f
==> Warning: Reinitializing MPD on this system will remove all MPD projects
==> Would you like to proceed with reinitialization? [y/N] y
==> Removed repository /home/knoepfel/.mpd
==> Using Spack instance at /scratch/knoepfel/spack
==> Added repo with namespace 'local-mpd'.
```

### A writeable Spack instance

If you do not have write access to the Spack instance you are using,
when invoking `spack mpd init` you will see an error like:

```console
==> Using Spack instance at /scratch/knoepfel/spack

==> Error: To use MPD, you must have a Spack instance you can write to.
           You do not have permission to write to the Spack instance above.
           Please contact scisoft-team@fnal.gov for guidance.
```

At this point, MPD does not yet support the creation of writeable
Spack instances as part of the initialization process.
