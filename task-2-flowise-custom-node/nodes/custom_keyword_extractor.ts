import { INode, INodeData, INodeParams } from 'flowise-components'
import nlp from 'compromise'

class KeywordExtractorNode implements INode {
    label: string
    name: string
    type: string
    description: string
    inputs: INodeParams[]
    outputs: string[]

    constructor() {
        this.label = 'Keyword Extractor'
        this.name = 'keywordExtractor'
        this.type = 'Custom'
        this.description = 'Extracts keywords from input text'
        this.inputs = [
            {
                label: 'Input Text',
                name: 'inputText',
                type: 'string'
            }
        ]
        this.outputs = ['string']
    }

    async run(nodeData: INodeData): Promise<string> {
        const text = nodeData.inputs?.inputText as string
        const doc = nlp(text)
        const nouns = doc.nouns().out('array')
        const uniqueKeywords = [...new Set(nouns)]
        return uniqueKeywords.join(', ')
    }
}

module.exports = { nodeClass: KeywordExtractorNode }
