import React from "react";

const SnippetItem = ({snippet}) => {
    return (
        <tr>
            <td>
                {snippet.id}
            </td>
            <td>
                {snippet.title}
            </td>
            <td>
                {snippet.owner}
            </td>
        </tr>
    )
}

const SnippetList = ({snippets}) => {
    console.log('snippets: ', snippets)
    const snippets1 = new Map(Object.entries(snippets))
    console.log('snippet1: ', snippets1)
    return (
        <table>
            <th>
                Id
            </th>
            <th>
                Title
            </th>
            <th>
                Owner
            </th>
            {snippets.map((snippet) => <SnippetItem snippet={snippet} />)}
        </table>
    )
}

export default SnippetList