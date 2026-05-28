# Deploy The Surf Log on Cloudflare Pages

Recommended host: **Cloudflare Pages**.

Why this one:

- Free for this static V1.
- No server process, so nothing goes to sleep or times out.
- Works with private GitHub repos.
- Automatic SSL.
- Cloudflare DNS handles apex/root domains cleanly.

## 1. Create the Pages project

1. Go to Cloudflare → **Workers & Pages** → **Create** → **Pages**.
2. Connect GitHub.
3. Pick repo: `jeffreydebolt/the-surf-log`.
4. Settings:
   - Production branch: `main`
   - Framework preset: `None`
   - Build command: leave blank
   - Build output directory: `/`
5. Deploy.

Cloudflare will give you a temporary URL like:

```text
the-surf-log.pages.dev
```

## 2. Put DNS on Cloudflare

Best path: use Cloudflare as DNS for `thesurflog.com`.

1. In Cloudflare, add site: `thesurflog.com`.
2. Cloudflare will give you two nameservers.
3. In Namecheap:
   - Domain List → `thesurflog.com` → Manage
   - Nameservers → Custom DNS
   - Paste the two Cloudflare nameservers
   - Save
4. Wait for nameserver propagation.

This avoids apex/root-domain weirdness at Namecheap and gives free SSL/proxying.

## 3. Add custom domains in Pages

In the Cloudflare Pages project:

1. Custom domains → Add:

```text
thesurflog.com
```

2. Add another:

```text
www.thesurflog.com
```

Cloudflare will create/validate the right DNS records. Keep both routed to the Pages project.

## 4. Expected DNS records

If Cloudflare does not create them automatically, use:

```text
CNAME  thesurflog.com      the-surf-log.pages.dev  proxied
CNAME  www                 the-surf-log.pages.dev  proxied
```

Cloudflare supports CNAME flattening at the apex/root, so this works for `thesurflog.com`.

## 5. Verify

After deployment/DNS:

```bash
curl -I https://thesurflog.com
curl -I https://www.thesurflog.com
```

You want HTTP `200` or a clean redirect, with HTTPS working.
