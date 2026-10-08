import { test, expect } from '@playwright/test';

test('health badge reflects v2 OK state for 72C sample', async ({ page }) => {
  await page.goto('/');
  const badge = page.locator('#health');
  await expect(badge).toHaveText('OK');
  await expect(badge).toHaveClass(/badge ok/);
});
