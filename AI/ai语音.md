# 基本概念







# ssml的基本规则

## speak根元素

`<speak>`：指定一个SSML文档的根元素，表示需要朗读的文本。

`speak` 元素包含版本、语言和标记词汇定义等信息。 `speak` 元素是所有 SSML 文档必需的根元素。 必须在 [`lang`](https://learn.microsoft.com/zh-cn/azure/ai-services/speech-service/speech-synthesis-markup-voice#adjust-speaking-languages) 元素内将 `speak` 指定为默认语言，无论是否在其他地方调整该语言。

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="string"></speak>
```

| 属性       | 说明                                                         | 必需还是可选 |
| :--------- | :----------------------------------------------------------- | :----------- |
| `version`  | 指示用于解释文档标记的 SSML 规范的版本。 当前版本为“1.0”。   | 必需         |
| `xml:lang` | 根文档的语言。 该值可以包含语言代码，例如 `en`（英语），也可以包含区域设置，例如 `en-US`（美国英语）。 | 必需         |
| `xmlns`    | 用于定义 SSML 文档的标记词汇（元素类型和属性名称）的文档的 URI。 当前 URI 为 "http://www.w3.org/2001/10/synthesis"。 | 必需         |



# Hello World

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        This is the text that is spoken.
    </voice>
</speak>
```



# ssml的标签

## 停顿



```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        Welcome <break /> to text to speech.
        Welcome <break strength="medium" /> to text to speech.
        Welcome <break time="750ms" /> to text to speech.
    </voice>
</speak>
```



| 属性       | 说明                                                         | 必需还是可选 |
| :--------- | :----------------------------------------------------------- | :----------- |
| `strength` | 使用以下值之一指定暂停的相对持续时间： <br />x-weak：250 毫秒<br />weak：500 毫秒<br />medium（默认值）： 750 毫秒<br />strong：1,000 毫秒<br />x-strong：1,250 毫秒 | 可选         |
| `time`     | 暂停的绝对持续时间，以秒为单位（例如 `2s`）或以毫秒为单位（例如 `500ms`）。 有效值的范围为 0 到 5000 毫秒。 如果设置的值大于支持的最大值，则服务将使用 `5000ms`。 ==如果设置了 `time` 属性，则会忽略 `strength` 属性。== | 可选         |





## 指定段落和句子

`p` 和 `s` 元素分别用于表示段落和句子。 如果缺少这些元素，则语音服务会自动确定 SSML 文档的结构。

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        <p>
            <s>Introducing the sentence element.</s>
            <s>Used to mark individual sentences.</s>
        </p>
        <p>
            Another simple paragraph.
            Sentence structure in this paragraph is not explicitly marked.
        </p>
    </voice>
</speak>
```





```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="string">
    <mstts:backgroundaudio src="string" volume="string" fadein="string" fadeout="string"/>
    <voice name="string" effect="string">
        <audio src="string"></audio>
        <bookmark mark="string"/>
        <break strength="string" time="string" />
        <emphasis level="value"></emphasis>
        <lang xml:lang="string"></lang>
        <lexicon uri="string"/>
        <math xmlns="http://www.w3.org/1998/Math/MathML"></math>
        <mstts:audioduration value="string"/>
        <mstts:express-as style="string" styledegree="value" role="string"></mstts:express-as>
        <mstts:silence type="string" value="string"/>
        <mstts:viseme type="string"/>
        <p></p>
        <phoneme alphabet="string" ph="string"></phoneme>
        <prosody pitch="value" contour="value" range="value" rate="value" volume="value"></prosody>
        <s></s>
        <say-as interpret-as="string" format="string" detail="string"></say-as>
        <sub alias="string"></sub>
    </voice>
</speak>
```



## 强调

`<emphasis>`：将重音（强调）添加到文本的某些部分。强调级别（`level`）可以是`strong`（强调）或`moderate`（中度强调）。

```xml

```



## Prosody

Prosody标签是Speech Synthesis Markup Language (SSML)中的一个标签，用于调整语音合成音频的声音特征和语调。

`<prosody>`：调整语音的音调（`pitch`）、轮廓（`contour`）、范围（`range`）、速度（`rate`）和音量（`volume`）。

```xml
<speak>
  <p>
    <s>This is a <prosody pitch="high">high pitched</prosody> sentence.</s>
    <s>This is a <prosody pitch="low">low pitched</prosody> sentence.</s>
  </p>
  <p>
    <s>This is a <prosody rate="fast">fast spoken</prosody> sentence.</s>
    <s>This is a <prosody rate="slow">slow spoken</prosody> sentence.</s>
  </p>
  <p>
    <s>This is a <prosody volume="+10%">loud</prosody> sentence.</s>
    <s>This is a <prosody volume="-10%">soft</prosody> sentence.</s>
  </p>
</speak>
```





`<mstts:backgroundaudio>`：设置背景音频的相关属性，如音频源（`src`）、音量（`volume`）、淡入（`fadein`）和淡出（`fadeout`）。

`<voice>`：指定要使用的语音模型的名称（`name`）和效果（`effect`）或风格。

\<audio>：指定一个外部音频文件的URL（src），用于在朗读期间播放。

`<bookmark>`：在特定位置添加一个标记，以便在播放期间进行导航。

`<break>`：指定中断的强度（`strength`）和时间（`time`）。



`<lang>`：指定文本的语言（`xml:lang`）。

`<lexicon>`：指定一个外部词典的URL（`uri`），以改善文本的发音。

`<math>`：在SSML文本中嵌入数学表达式的MathML表示。

`<mstts:audioduration>`：指定语音合成音频的持续时间（`value`）。

`<mstts:express-as>`：设置文本的朗读方式，如风格（`style`）、风格程度（`styledegree`）和角色（`role`）。

`<mstts:silence>`：插入一段静音。可以设置静音的类型（`type`）和持续时间（`value`）。

`<mstts:viseme>`：指定发音中使用的Viseme类型（`type`）。

<p>：表示一个段落。

`<phoneme>`：指定一个音素（`ph`），用于更精确地控制发音。可以选择指定使用的音素表（`alphabet`）。



`<say-as>`：指定要以特定方式解释或显示的文本。可选择指定的解释类型（`interpret-as`）、格式（`format`）和详细程度（`detail`）。

`<sub>`：指定一个替换文本（`alias`）来代替原始文本。

以上是对标签的基本解释。请注意，具体的属性和值可能会根据你使用的语音合成引擎或语言而有所不同。



