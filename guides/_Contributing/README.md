---
title: 'How to: Bæta við leiðbeiningum'
---

# Leiðbeiningar

Leiðbeiningar eru bara basic [Markdown](https://markdownlivepreview.com/).

Allar leiðbeiningar eru geymdar undir `/guides` möppunni.

Undirmöppur eru flokkarnir `/guides/<FLOKKUR>` og eru leiðbeiningarnar settar í þær undirmöppur.
Þannig að nýjar leiðbeiningar eru stofnaðar undir: `/guides/<FLOKKUR>/<EitthvaðNafn>.md`


## Front Matter

Allar leiðbeiningar þurfa að hafa __front matter__ efst í skjali:

```
---
title: '<Titillinn á leiðbeiningunum>'
---
```

Mikilvægt að hafa _title_ til staðar, annars munu leiðbeiningar ekki birtast á síðu.

## Búa til nýjar leiðbeiningar:

1. Búa til nýtt skjal einhversstaðar undir `/guides/<FLOKKUR>/<nafnáskjali>.md`
2. Skilgreina titilinn í __front matter__ skjalsins
3. Skrifa leiðbeiningarnar í [Markdown](https://markdownlivepreview.com/)
4. Vista
5. Push-a á github

## Deployment

Þegar síða er deployed á github pages sér eitt skrefið um að keyra compile-nav.py
um að uppfæra listann yfir leiðbeiningar sem birtar eru á síðunni. Ef allt er gert
rétt þá munu nýju leiðbeiningarnar birtast.


![Bleiki Víkingurinn](/assets/images/_Contributing/tpvvector.svg)

