title: Combinators in CSS
date: 2020-10-22 07:58
author: Punit Jain
Category: Javascript
Slug: Combinators in CSS
Summary: Combinators in CSS
Tags: CSS
Authors: Punit Jain
Status: published

# Combinators in CSS

There are 4 key combinators in CSS:
1. Adjacent Sibling
2. General Sibling
3. Child Combinator
4. Descendant Combinator

## Adjacent Sibling

The adjacent sibling follow below format:
```css
h2 + p {
  color: blue;
}
```
applied to html:
```html
<div>
  <h2>Topic of the Day</h2>
  <p>CSS Adjacent Sibling applied</p>
  <h2>Sub Topic</h2>
  <h3>nested header</h3>
  <p>Not a CSS Adjacent Sibling</p>
  <h2>new subtopic</h2>
  <p>CSS Adjacent Sibling applied</p>
</div>
```

The elements should share the same parent and should follow the the first element. 
In this case p must follow h2 tag.

## General Sibling

The adjacent sibling follow below format:
```css
h2 ~ p {
  color: blue;
}
```
applied to html:

```html
<div>
  <h2>Topic of the Day</h2>
  <p>CSS General Sibling applied</p>
  <h2>Sub Topic</h2>
  <h3>nested header</h3>
  <p>CSS General Sibling even tough nested inside a h3</p>
</div>
```

In this case elements share the same parent and second element comes after the first.
The second element doesnot have to come directly after the first tough.

## Child Combinator

The adjacent sibling follow below format:
```css
div > p {
  color: blue;
}
```
applied to html:

```html
<div>
  <div>Topic of the Day</div>
  <p>CSS Child combinator applied</p>
  <div>New Topic</div>
  <input />
  <p>CSS not applied</p>
</div>
```

Any para which is direct child of a div will get the style applied.
Here second para doesnot have style applied as para is not a direct child of div element.

## Descendant Combinator

The adjacent sibling follow below format:
```css
div p {
  color: blue;
}
```
applied to html:

```html
<div>
  <div>Topic of the Day</div>
  <p>CSS descendant combinator applied</p>
  <div>New Topic</div>
  <article>
  <p>CSS descendant combinator applied here as well</p>
  </article>
</div>
```

In this case the descendant combinator is applied to both para as they are descendant of div.
It doesnot matter whether they are direct descendant of div elements but should be descendants.
