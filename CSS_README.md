# StackIt Q&A Forum - Modern CSS Design System

## Overview

This comprehensive CSS design system provides a modern, responsive, and accessible interface for the StackIt Q&A forum platform. The design features a clean, professional appearance with smooth animations, excellent mobile responsiveness, and optional dark mode support.

## Features

### 🎨 **Modern Design**
- Clean, minimalist interface with subtle shadows and rounded corners
- Professional color scheme with CSS custom properties
- Smooth hover effects and transitions
- Beautiful typography using Inter font

### 📱 **Fully Responsive**
- Mobile-first design approach
- Optimized for all screen sizes (mobile, tablet, desktop)
- Collapsible navigation on mobile devices
- Touch-friendly buttons and interactive elements

### 🌙 **Dark Mode Support**
- Toggle between light and dark themes
- Persistent theme preference using localStorage
- Smooth transitions between themes
- Optimized colors for both light and dark modes

### ♿ **Accessibility**
- High contrast ratios for better readability
- Focus indicators for keyboard navigation
- Screen reader friendly markup
- Semantic HTML structure

### ⚡ **Performance**
- CSS custom properties for efficient theming
- Optimized animations and transitions
- Minimal CSS footprint
- Fast loading times

## File Structure

```
static/
├── main.css              # Main stylesheet with all components
├── dark-mode.css         # Dark mode overrides
├── light.css             # Legacy light theme (deprecated)
└── dark.css              # Legacy dark theme (deprecated)
```

## CSS Custom Properties

The design system uses CSS custom properties for consistent theming:

### Colors
```css
--primary-color: #6366f1;      /* Main brand color */
--primary-hover: #4f46e5;      /* Hover state */
--primary-light: #e0e7ff;      /* Light background */
--success-color: #10b981;      /* Success states */
--error-color: #ef4444;        /* Error states */
--warning-color: #f59e0b;      /* Warning states */
```

### Typography
```css
--font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
--font-size-base: 1rem;
--font-size-lg: 1.125rem;
--font-size-xl: 1.25rem;
```

### Spacing
```css
--spacing-1: 0.25rem;          /* 4px */
--spacing-2: 0.5rem;           /* 8px */
--spacing-4: 1rem;             /* 16px */
--spacing-6: 1.5rem;           /* 24px */
```

### Border Radius
```css
--radius-sm: 0.375rem;         /* 6px */
--radius-md: 0.5rem;           /* 8px */
--radius-lg: 0.75rem;          /* 12px */
--radius-xl: 1rem;             /* 16px */
```

## Components

### Navigation Bar
- Sticky positioning with backdrop blur
- Responsive collapse on mobile
- Smooth hover effects
- Theme toggle button

### Cards
- Subtle shadows and rounded corners
- Hover animations
- Consistent spacing
- Flexible content areas

### Buttons
- Multiple variants (primary, outline, success, danger)
- Hover and focus states
- Different sizes (sm, default, lg)
- Icon support

### Forms
- Clean input styling
- Focus indicators
- Validation states
- Consistent spacing

### Alerts
- Color-coded messages
- Dismissible functionality
- Left border accents
- Accessible design

### Question Items
- Featured design with left accent border
- Hover animations
- Meta information display
- Tag styling

## Usage

### Basic Implementation
The CSS is automatically loaded in the base template:

```html
<link href="/static/main.css" rel="stylesheet">
```

### Theme Toggle
The dark mode toggle is included in the navbar:

```html
<button class="nav-link btn btn-link" id="themeToggle">
    <i class="fas fa-moon" id="themeIcon"></i>
</button>
```

### Utility Classes
Use these utility classes for quick styling:

```html
<!-- Colors -->
<div class="text-primary">Primary text</div>
<div class="bg-success">Success background</div>

<!-- Spacing -->
<div class="p-4">Padding</div>
<div class="m-2">Margin</div>

<!-- Borders -->
<div class="rounded-lg">Rounded corners</div>
<div class="border">Border</div>

<!-- Shadows -->
<div class="shadow-sm">Small shadow</div>
<div class="shadow-lg">Large shadow</div>
```

## Responsive Breakpoints

- **Mobile**: < 576px
- **Tablet**: 576px - 768px
- **Desktop**: > 768px

## Browser Support

- Chrome 88+
- Firefox 87+
- Safari 14+
- Edge 88+

## Customization

### Changing Colors
To customize the color scheme, modify the CSS custom properties in `main.css`:

```css
:root {
    --primary-color: #your-color;
    --primary-hover: #your-hover-color;
    /* ... other colors */
}
```

### Adding New Components
Create new component styles following the existing pattern:

```css
.your-component {
    background: var(--white);
    border: 1px solid var(--gray-200);
    border-radius: var(--radius-lg);
    padding: var(--spacing-4);
    transition: all var(--transition-normal);
}

.your-component:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-1px);
}
```

### Dark Mode Overrides
Add dark mode styles to `dark-mode.css`:

```css
.your-component {
    background: #1e293b;
    border-color: #334155;
    color: #f1f5f9;
}
```

## Best Practices

1. **Use CSS Custom Properties**: Always use the defined variables for consistency
2. **Mobile First**: Design for mobile first, then enhance for larger screens
3. **Accessibility**: Ensure proper contrast ratios and focus indicators
4. **Performance**: Keep animations smooth and lightweight
5. **Semantic HTML**: Use proper HTML structure for better accessibility

## Troubleshooting

### Theme Not Switching
- Check if localStorage is enabled in the browser
- Verify the dark-mode.css file is accessible
- Check browser console for JavaScript errors

### Styling Issues
- Ensure Bootstrap CSS is loaded before main.css
- Check for conflicting CSS rules
- Verify CSS custom properties are supported

### Mobile Issues
- Test on actual devices, not just browser dev tools
- Check viewport meta tag is present
- Verify touch targets are large enough (44px minimum)

## Future Enhancements

- [ ] CSS Grid layout for advanced layouts
- [ ] CSS-in-JS integration
- [ ] Advanced animation library
- [ ] Component library documentation
- [ ] Design token system
- [ ] Automated accessibility testing

## Credits

- **Font**: Inter by Google Fonts
- **Icons**: Font Awesome 6
- **Framework**: Bootstrap 5
- **Design System**: Custom built for StackIt

---

For questions or contributions, please refer to the project documentation or contact the development team. 