using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class planet_generator : MonoBehaviour
{
    public GameObject planet;

    // Start is called before the first frame update
    void Start()
    {
        int i;
        for (i = 1;  i < 9; i++)
        {
            planet.name = i.ToString();
            Instantiate(planet);

        }
        



    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
