## Golang Implementation
Golang has many advantages: safe, reliable, creating only one executable file output after the compilation without any dependencies, etc.
The Feilong doesn't have a golang client library, but it provides a lot of Rest API. The z/vm will use rest instead. To be noticed, the `Querying` part is different from python-implementation:
```sh
# Rest
GET /   # API version
GET /host   # Host infomation
GET /guests #Guest list
GET /guests/{userid}/info
GET /guests/stats   # Get guests network interface statistics.
GET  /guests/nics
```
After processing metrics, the golang exporter uses the [Prothemethus golang client](https://github.com/prometheus/client_golang/). I would copy the config files from the old version(port 9110).

## *(Idea 1) Contribute a golang version zvmconnector*
Just rewrite the `zvmconnector` in golang. I have already started the golang version in my [repo](https://github.com/kaiakz/zvmconnector-golang/). I would like to contribute the project, and use it as the library in the new z/vm exporter(golang version).
`zvmconnector-golang` provides simple APIs:
```golang
type Response struct {
	Rs        int    `json:"rs"`        // The reason code for API request.
	OverallRC int    `json:"overallRC"` // The overall return code for API request.
	ModID     int    `json:"modID"`     // The module ID that causes the error to occur.
	Rc        int    `json:"rc"`        // The return code for API request.
	Errmsg    string `json:"errmsg"`    // The error message returned for API request. It can be empty if no error occur.
	Output    string `json:"output"`    // The return data from API request.
}

type Connect interface {
	Fetch(apiName string, apiArgs []string, apikArgs map[string]interface{}) Response
	Close()
}

func NewConnector(ip string, port uint16, timeout time.Duration, isRest bool) (Connect, error)
```
It supports setting a rest or socket connection with the Feilong.