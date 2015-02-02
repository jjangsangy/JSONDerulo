# JSONDerulo
A JSON serialization that is dirty to talk about

## Author: Sang Han 2015
jjangsangy@gmail.com

```sh
$ derulo
{
  "JSONDerulo": "JSONDerulo"
}
```

## Usage

```sh
$ derulo --say
{
  "JSONDerulo": "whatcha say"
}
```

### Syntactic Sugar

```sh
$ derulo --say --output=json
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
        "yeah it's like": [
            "S", "O", "L", "O",
            "S", "O", "L", "O",
            "S", "O", "L", "O",
            "S", "O", "L", "O"
      ],
      "yeah it's like": [
            "S", "O", "L", "O",
            "S", "O", "L", "O",
            "S", "O", "L", "O",
            "S", "O", "L", "O"
      ],
      "yeah it's like":  [ ...
      

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
