<!--- Copyright (c) 2021 Valentin Weber

    This file is part of the software mendeley-watchdog.

    The software is licensed under the European Union Public License
    (EUPL) version 1.2 or later. You should have received a copy of
    the english license text with the software. For your rights and
    obligations under this license refer to the file LICENSE or visit
    https://joinup.ec.europa.eu/community/eupl/og_page/eupl to view
    official translations of the licence in another language of the EU.
--->

# Python Atom Feed
This will eventually be a generator (and maybe parser) for atom feeds as
specified [rfc4287][rfc4287]. As of right now the generator does not support
the atom extensions defined in Section 6 of the specification.

In order to create pretty XML for easier readability this generator uses
[lxml][lxml] which depends on the *libxml2* and *libxslt* libraries. Those may
have to be installed separately.

[rfc4287]: https://datatracker.ietf.org/doc/html/rfc4287
[lxml]: https://pypi.org/project/lxml/