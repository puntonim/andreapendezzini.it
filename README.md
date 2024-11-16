# **andreapendezzini.it**

Andrea Pendezzini frontend fro the web app deployed at: https://andreapendezzini.it

With HTML and vanilla JavaScript.

# IMPORTANT

This source code resides in the private repo: https://github.com/puntonim/andrea-pendezzini-monorepo.
Do not ever checkout and push code to https://github.com/puntonim/andreapendezzini.it/ but instead use
the private repo.

## So why does this repo even exist?

Since GitHub Pages can only exist in free _public_ repos then when deploying the
frontend, the FE code is force-pushed to this public repo.

# Urls

- https://github.com/puntonim/andreapendezzini.it
- https://puntonim.github.io/andreapendezzini.it

## DNS Record at Gandi

```
@ 1800 IN A 185.199.108.153
@ 1800 IN A 185.199.109.153
@ 1800 IN A 185.199.110.153
@ 1800 IN A 185.199.111.153
www 1800 IN CNAME andreapendezzini.it.
```

# FE Deployment

```shell
$ make deploy
```

# Copyright

Copyright Andrea Pendezzini and puntonim (https://github.com/puntonim). No License.
