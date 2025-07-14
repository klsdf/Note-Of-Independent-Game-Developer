```c#
using UnityEngine.EventSystems;
void OnMouseDown()
    {
        if (IsTouchedShopUI())
        {
            return;
        }

      
    }

    private bool IsTouchedShopUI()
    {
        PointerEventData pointerEventData = new PointerEventData(eventSystem);
        pointerEventData.position = Input.mousePosition;

        List<RaycastResult> results = new List<RaycastResult>();
        raycaster.Raycast(pointerEventData, results);

        foreach (RaycastResult result in results)
        {
            
            if(result.gameObject.name.Contains("ShopPenal"))
            {
                return true;
            }
            // Debug.Log($"Clicked on ShopCard UI!{result.gameObject.name}");


        }
        return false;
    }


```