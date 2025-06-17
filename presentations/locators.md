---
class: inverse, center, middle
# Komponensek kijelölése
---

## Komponensek kijelölése

- Id alapján
- Name alapján
- Link szövege alapján
  - Link szövegének egy részlete alapján
- CSS class name
- CSS selector
  - Developer tools/Inspector/Copy CSS selector
- Tag neve alapján
- XPath
  - Developer tools/Inspector/Copy XPath
- Saját attribútum, pl. `data-testid`, `data-test`, `data-qa`
  - CSS selectorral és XPath kifejezéssel is lekérhető

https://www.selenium.dev/documentation/webdriver/elements/locators/

---

## XPath

- W3C szabvány
- Egy XML dokumentum elemei és attribútumai közötti navigációt biztosítja
- XPath szintaktika segítségével definiálhatjuk az XML dokumentum részeit
- Kifejezések segítségével mozoghatunk az XML dokumentumban
- https://codebeautify.org/Xpath-Tester
- Kipróbálás: DevTools / Elements / `Ctrl + F`

---

## XPath példák

- `/html`
- `/html/body`
- `//input`
- `/html/@lang`

---

## XPath predicates 1.

- `/html/table/tbody/tr[1]` - első `tr`
- `/html/table/tbody/tr[last()]` - utolsó `tr`
- `/html/table/tbody/tr[last() - 1]` - utolsó előtti `tr`
- `/html/table/tbody/tr[position() < 3]` - első két `tr`

---

## XPath predicates 2.

- `//input[@id]` - van `id` attribútuma
- `//input[@id="name-input"]` - `id` attribútumának értéke `name-input`

---

## Lekérdezés tartalom alapján

- `//button[text()='Announce']`

---

## XPath ismeretlen csomópontok

- `/html/body/*` - összes gyerek
- `//*` - összes elem
- `//*[@id="name-input"]` - összes tag, megadott attribútummal

---

## CSS selector (basic selectors)

- CSS-ben az elemek kijelölésére, melyekre valamilyen formátumot szeretnénk alkalmazni
- W3C CSS specifikáció része
- Kipróbálás: DevTools / Elements / `Ctrl + F`

```plaintext
Lekérdezés id alapján (id selector)
CSS: #example
XPath: //div[@id='example']
```

```plaintext
Lekérdezés tag alapján (type selector)
CSS: input
XPath: //input
```

```plaintext
Lekérdezés class alapján (class selector)
CSS: .example
XPath: //div[@class='example']
```

```plaintext
Lekérdezés attribútum alapján (attribute selector)
CSS: [name='username']
XPath: //div[@name='username']
```

```plaintext
Mindent lekérdez (universal selector)
CSS: *
XPath: //
```

## CSS attribute selectors

- `[attr]` - létező attribútum
- `[attr=value]` - megegyező értékű attribútum
- `[attr~=value]` - szavakból álló attribútum egyik szava
- `[attr|=value]` - értéke vagy a `value`, vagy `value-` és utána bármilyen érték
- `[attr^=value]` - `value` értékkel kezdődik
- `[attr$=value]` - `value` értékkel végződik
- `[attr*=value]` - legalább egyszer tartalmazza
- `[attr operator value i]` - összehasonlítás kis- és nagybetű független (csak ASCII-ra)
- `[attr operator value s] ` - összehasonlítás kis- és nagybetű függő (csak ASCII-ra)

- `id` attribútum alapján: `css=tag#id`, pl. `css=input#name-input`
- CSS class alapján: `css=tag.class`, pl. `css=input.btn`, vagy tag nélkül `.btn`
- Attribútum érték alapján `css=tag[attribute=value]`, pl. `css=input[type=submit]`

---

## Grouping selectors

```plaintext
CSS: div, span
Eredménye: összes div és span csomópont
```

---

## Combinators

```plaintext
Descendant combinator
CSS: div span
XPath: //div//span
Eredménye: összes div csomópontban lévő span csomópont
```

```plaintext
Child combinator
CSS: div > span
XPath: //div/span
Eredménye: összes közvetlenül a div csomópontban lévő span csomópont
```

```plaintext
General sibling combinator
CSS: div ~ span
Eredménye: span csomópont, ami testvérként követi a div csomópontot
```

```plaintext
Adjacent sibling combinator
CSS: div + span
XPath: //div/following-sibling:span[1]
Eredménye: span csomópont, ami testvérként közvetlenül követi a div csomópontot
```

```plaintext
Column combinator
CSS: col || td
Eredménye: a col csomóponthoz tartozó összes td csomópont
```

## Pseudo classes

```plaintext
Pseudo classes - nem részei a DOM fának
CSS: a:visited
Eredménye: összes meglátogatott a csomópont
```

https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes

```plaintext
CSS: #recordlist li::nth-of-type(4)
Eredmény: negyedik li gyermeke a #recordlist csomópontnak
CSS: #recordlist li::nth-child(4)
Eredmény: negyedik gyermeke a #recordlist csomópontnak, ha az li csomópont
CSS: #recordlist *::nth-child(4)
Eredmény: negyedik gyermeke független a típusától
```

```plaintext
Pseudo elements - HTML-ben nem szereplő elemek
CSS: p::first-line
Eredménye: p csomópont első sora
```

https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements

---

## Locator best practices

- Ahol lehet kérdezzünk le id alapján, mert gyors és egyértelmű
- Ha id nincs, akkor preferáljuk a CSS selector használatát
- Az XPath nagyon kifejező, de bonyolult a szintaxis, és általában a böngészőkben
  nincs teljesítményhangolva, így lassú lehet
- XPath-szal lehet tartalom alapján (`text()`, attribútum érték) keresni, CSS
  selectorral nem
- Link szövege alapján csak linket lehet találni
- Tag neve alapján veszélyes lehet, hiszen tipikusan több
