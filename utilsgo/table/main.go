package table

import (
    "encoding/json"
    "errors"
    "strings"
    "j2t"
)

func Table(tableData any, headers []string) (string, error) {
    jsonBytes, err := json.Marshal(tableData)
    if err != nil {
        return "", err
    }

    emtyStr := ""
    replacer := strings.NewReplacer("𒀸", emtyStr)
    jsonStr := replacer.Replace(string(jsonBytes))

    if ok, html := j2t.JSON2HtmlTable(jsonStr, headers, []string{}); ok {
        return html, nil
    } else {
        return "", errors.New("failed to convert table data to html table")
    }
}
