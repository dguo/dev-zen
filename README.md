# Dev Zen
Dev Zen is a suggestion for local software development. It is also an
**optional** executable that can make following the suggestion slightly easier.

## How
* Use [Docker](https://www.docker.com/what-docker) and [Docker
  Compose](https://docs.docker.com/compose/) to create a development environment
* Create a mini-[CLI](https://en.wikipedia.org/wiki/Command-line_interface) for
  working on a particular project
    * Distribute this CLI as a `dev` script in the project's root directory

## Why
* The actual process of software development should fade into the background
* The problem that is being solved or the goal that we have in mind should be
  the focus of our attention
* Distractions (like figuring out how to install a language or database locally)
  should be mitigated as much as possible
* Making a project easy to work on is good for both the original developers and
  any future collaborators
* Commands over documentation
    * A CLI lets a developer immediately know what is possible (`$ ./dev -h`)
    * Improvements to the development workflow can be baked into the CLI rather
      than having to inform all the developers of changes

## Examples
* Work in progress

## Advantages
* [Infrastructure as code](https://martinfowler.com/bliki/InfrastructureAsCode.html)
    * Your development environment is versioned and changes in lockstep with
      your code
* Docker is [cross-platform](https://docs.docker.com/engine/installation/)
    * Especially after the native versions for Mac and Windows
      [were released](https://blog.docker.com/2016/07/docker-for-mac-and-windows-production-ready/)
* Volume mounting allows you to use the editors/tooling you are familiar with
    * File changes will automatically get synced into the running Docker container(s)
* Your machine stays clean
    * You don't need to install anything besides Docker
* Each project gets an isolated development environment
    * You can have projects simultaneously running in different versions of the
      same language without affecting each other
* By using Docker for development, it will be easy to also use it for
  [CI](https://en.wikipedia.org/wiki/Continuous_integration),
  [CD](https://en.wikipedia.org/wiki/Continuous_delivery), and production
* It's optional
    * Someone who doesn't want to use Docker or the CLI doesn't necessarily
      have to

## Possible Caveats
* Need to learn how to use Docker and Docker Compose
* Could be overkill if you're only really working on one project at a time or if
  you only use one language or technology

## Tips
* Use [Python](https://www.python.org/) for the `dev` script
    * More powerful and easier to maintain compared to a shell language (like
      [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) or
      [Zsh](https://en.wikipedia.org/wiki/Z_shell))
    * Pretty much every machine is going to have Python installed
    * Has an extensive standard library
    * It's easy to create a CLI (with subcommands!) using [argparse](https://docs.python.org/3/library/argparse.html)
    * Stick to the standard library so that you and any collborators don't have
      to install anything else
* [Ruby](https://www.ruby-lang.org/) should also work well since it includes
  [OptionParser](http://ruby-doc.org/stdlib-2.4.0/libdoc/optparse/rdoc/OptionParser.html)

## Executable
* Put this [Bash script](bash/dev) in your
  [PATH](https://en.wikipedia.org/wiki/PATH_(variable))
* It checks the working directory for the presence of an executable `dev` script
  and runs it if it exists
* This means you can run it without `./` (so `$ dev` instead of `$ ./dev`)

## Docker alternatives
* Installing whatever you need
    * Usually straightforward
    * No indirection
    * But then it's probably not portable, easily reproducible, isolated, etc.
* [virtualenv](https://virtualenv.pypa.io/en/stable/), [rbenv](https://github.com/rbenv/rbenv), [nvm](https://github.com/creationix/nvm), [rustup](https://www.rustup.rs/), etc.
    * Reasonable solution for each particular language
    * But these tools don't help with other software, such as [Postgres](https://www.postgresql.org/) and [Redis](https://redis.io/)
    * And you need one for each language
* [Vagrant](https://www.vagrantup.com/)
    * Not helpful for production environments
    * Running a full [VM](https://en.wikipedia.org/wiki/Virtual_machine) is
      resource intensive and slow to start up
* [Vagga](http://vagga.readthedocs.org/)
    * It also values a
      [command-centric workflow](https://vagga.readthedocs.io/en/latest/vagga_features.html#command-centric-workflow)
    * The author considers it beta quality software

## `dev` alternatives
* [Make](https://www.gnu.org/software/make/)
    * Need to use Make's syntax
    * Can't generate help output
* Documenting commands
    * Good documentation is awesome, but it's easier to run `$ dev -h` than to
      copy a command from a README or wiki
* [IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment)
