using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class planet : MonoBehaviour
{
    public AudioSource audio_source;


    public float orbit_time;
    public float orbit_distance;
    public float diameter;

    private float sun_allowance = 10;

    public Material mercury;
    public Material venus;
    public Material earth;
    public Material mars;
    public Material jupiter;
    public Material saturn;
    public Material uranus;
    public Material neptune;

    public AudioClip terrestrial;
    public AudioClip gas_giant;

    private float time_through = 0;
    private float degrees_through = 0;

    private Vector3 correct_pos;
    private Renderer mesh_renderer;
    private TrailRenderer tr;
    // Start is called before the first frame update
    void Start()
    {

        // use text file from nasa exeoplanetary data to get orbit stuff


        tr = GetComponent<TrailRenderer>();

        mesh_renderer = GetComponent<Renderer>();
        if (gameObject.name == "1(Clone)")
        {
            orbit_time = 0.241f;
            orbit_distance = 0.387f;
            diameter = 0.383f;
            mesh_renderer.material = mercury;
            audio_source.clip = terrestrial;
        }
        if (gameObject.name == "2(Clone)")
        {
            orbit_time = 0.615f;
            orbit_distance = 0.723f;
            diameter = 0.949f;
            mesh_renderer.material = venus;
            audio_source.clip = terrestrial;
        }
        if (gameObject.name == "3(Clone)")
        {
            orbit_time = 1f;
            orbit_distance = 1f;
            diameter = 1f;
            mesh_renderer.material = earth;
            audio_source.clip = terrestrial;
        }
        if (gameObject.name == "4(Clone)")
        {
            orbit_time = 1.88f;
            orbit_distance = 1.52f;
            diameter = 0.532f;
            mesh_renderer.material = mars;
            audio_source.clip = terrestrial;
        }
        if (gameObject.name == "5(Clone)")
        {
            orbit_time = 11.9f;
            orbit_distance = 5.2f;
            diameter = 11.21f;
            mesh_renderer.material = jupiter;
            audio_source.clip = gas_giant;
        }
        if (gameObject.name == "6(Clone)")
        {
            orbit_time = 29.4f;
            orbit_distance = 9.57f;
            diameter = 9.45f;
            mesh_renderer.material = saturn;
            audio_source.clip = gas_giant;
        }
        if (gameObject.name == "7(Clone)")
        {
            orbit_time = 83.7f;
            orbit_distance = 19.17f;
            diameter = 4.01f;
            mesh_renderer.material = uranus;
            audio_source.clip = gas_giant;
        }
        if (gameObject.name == "8(Clone)")
        {
            orbit_time = 173.6f;
            orbit_distance = 30.18f;
            diameter = 3.88f;
            mesh_renderer.material = neptune;
            audio_source.clip = gas_giant;
        }
        tr.time = diameter / 2;
        //audio_source = GetComponent<AudioSource>();

        audio_source.pitch = 4/orbit_time;
        audio_source.volume = diameter / 12;
        

        

        transform.localScale = new Vector3(diameter/2, diameter / 2, diameter / 2);

        time_through = orbit_time / 2.5f;
        audio_source.Play();
    }

    // Update is called once per frame
    void Update()
    {
        time_through = time_through + Time.deltaTime;
        if (time_through > orbit_time)
        {
            time_through = 0;
        }
        degrees_through = (time_through / orbit_time)*2*Mathf.PI;
        correct_pos = new Vector3(Mathf.Sin(degrees_through) * (orbit_distance * 5 + sun_allowance), 0, Mathf.Cos(degrees_through) * (orbit_distance * 5 + sun_allowance));
        transform.position = correct_pos;
        
    }
}
