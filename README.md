# JSONDerulo
A JSON serialization that is dirty to talk about

```sh
$ derulo
{
  "JSONDerulo": "JSONDerulo"
}
```

## Author: Sang Han 2015

Made at UCSB Hack 2015 for fun
(_This software doesn't actually exist_)

## Usage


```sh
$ derulo [--version, -v]
  "JSONDerulo version JSONDerulo" 
  
```

# Basic Usage
```sh
$ derulo --say
```
```JSON
{
  "JSONDerulo": "whatcha say"
}
```

## Syntactic Sugar
```sh
$ derulo --say --output=json
```
```JSON
{
  "JSONDerulo": "whatcha say"
}
` ``

# Keyword Based Usage

```sh
$ derulo relationships
```
{
  "JSONDerulo": "JSONDerulo"
}
```
```sh
# derulo castle
```
```JSON
{
  "JSONDerulo": "IS THERE SUCH A THING AS A CONNECTED CASTLE?",
}

```

## Stream Output
```sh
$ derulo --stream solo
```
```JSON
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


## Known Issues

Infinite recursive calls

```
$ derulo --say derulo
```
```JSON
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

# Undefined Stochastic Behavior
``` sh
$ derulo advice
```
```JSON
{
  "JSONDerulo": "Marry Me"
}
```


```sh
$ derulo advice
```
```JSON
{
  "JSONDerulo": "Marry Me"
}
```
