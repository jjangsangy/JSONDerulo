# JSONDerulo
A JSON serialization that is dirty to talk about

## Author: Sang Han 2015:
Made at UCSB Hack 2015 for fun

```sh
$ derulo
{
  "JSONDerulo": "JSONDerulo"
}
```

## Usage

```sh
$ derulo [--version, -v]
  "JSONDerulo version JSONDerulo" 
```

# Basic Usage
```sh
$ derulo --say
{
  "JSONDerulo": "whatcha say"
}
```

Syntactic Sugar

```sh
$ derulo --say --output=json
```
```JSON
{
  "JSONDerulo": "whatcha say"
}
```

Keyword Based Query

```sh
$ derulo relationships
{
  "JSONDerulo": "JSONDerulo"
}
```

```sh
# derulo castle
{
  "JSONDerulo": "IS THERE SUCH A THING AS A CONNECTED CASTLE?",
}

```

## Stream Output
```sh
$ derulo --stream solo
  "JSONDerulo": 
      [
        "Riding solo, soooooloooo",
        "yeah it's like",
            "S", "O", "L", "O",
            "S", "O", "L", "O",
            "S", "O", "L", "O",
            "S", "O", "L", "O"
      ]
}

```


## Some Known Issues

Issue with Infinite recursive calls

```sh
$ derulo --say derulo
{
  "JSONDerulo": {
    "JSONDerulo": {
      "JSONDerulo": {
        "JSONDerulo": {
          "JSONDerulo": {
            "JSONDerulo": ...
          }
        }
      }
    }
  }
}}
```

### Some Undefined Stochastic Behavior

``` sh
$ derulo
{
  "JSONDerulo": "JSONDerulo"
}
```

``` sh
$ derulo
{
  "JSONDerulo": "Marry Me"
}
```
