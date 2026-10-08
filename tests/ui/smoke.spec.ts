import { test, expect } from '@playwright/test';
test('starter thermal console renders', async ({ page }) => { await page.goto('/'); await expect(page.getByRole('heading',{name:'Thermal Console'})).toBeVisible(); await expect(page.locator('#reading')).toHaveText('72'); });
test('health badge reflects v2 Health', async ({ page }) => { await page.goto('/'); const badge = page.locator('#health'); await expect(badge).toHaveText('OK'); await expect(badge).toHaveClass(/\bok\b/); });
