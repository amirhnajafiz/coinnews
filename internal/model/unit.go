package model

type Unit struct {
	Name  string `koanf:"name"`
	Value int    `koanf:"value"`
	Type  string `koanf:"type"`
}
