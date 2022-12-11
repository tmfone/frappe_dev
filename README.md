## Frappe Development Tools

### Installation

```bash
$ bench get-app http://github.com/tmfone/frappe_dev
$ bench install-app frappe_dev --site [site_name]
```

### List of features
All feautures should be used on development environments only.

* To get a list of all whitelisted methods use following endpoint:

```api
GET /api/method/frappe_dev.tmf_toolbox.utils.get_whitelisted_methods
```

## License

see [LICENSE.md](LICENSE.md)