using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class camera : MonoBehaviour
{
    private Vector3 start_pos = new Vector3(0,10,-250);
    private Vector3 direction = new Vector3(0,1f,3f);
    private float distance;


    // Start is called before the first frame update
    void Start()
    {
        transform.position = start_pos;
    }

    // Update is called once per frame
    void Update()
    {
        distance = -transform.position.z;
        if (distance > 25)
        {
            transform.Translate(direction * Time.deltaTime);
            

        }
        if (Input.mousePosition.y / 100 > 0)
        {
            Time.timeScale = Input.mousePosition.y / 100;
        }
        
        
    }

}
