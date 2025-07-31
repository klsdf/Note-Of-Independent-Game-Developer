

核心就是将所有坐标都转屏幕坐标




```c#
  private IEnumerator MoveToCoroutine(Transform target, string speakText)
    {
        while (target != null)
        {
            Vector2 targetWorldPos;
            if (target is RectTransform)
            {
                targetWorldPos = ((RectTransform)target).position;
            }
            else
            {
                targetWorldPos = Camera.main.WorldToScreenPoint(target.position);
            }

            float distance = Vector2.Distance(rectTransform.position, targetWorldPos);
            if (distance > arriveThreshold)
            {
                Vector2 nextPos = Vector2.MoveTowards(rectTransform.position, targetWorldPos, moveSpeed * Time.deltaTime);
                rectTransform.position = nextPos;
                yield return null;
            }
            else
            {
                rectTransform.position = targetWorldPos;
                break;
            }
        }
        if (!string.IsNullOrEmpty(speakText))
        {
            Speak(speakText);
        }
        moveCoroutine = null;
    }

```